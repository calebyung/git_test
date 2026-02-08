import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')


def train_surrogate_tree(df, xgb_proba_col='xgboost_proba'):
    """
    Train a surrogate decision tree to approximate XGBoost probabilities.
    
    Args:
        df: DataFrame with columns [features..., original_binary_target, 
                                   xgboost_proba, proba_interval_start, proba_interval_end]
        xgb_proba_col: Name of the column containing XGBoost probabilities
    
    Returns:
        trained_model, evaluation_results
    """
    # Identify feature columns (exclude known non-feature columns)
    exclude_cols = ['original_binary_target', xgb_proba_col, 'proba_interval_start', 'proba_interval_end']
    feature_cols = [col for col in df.columns if col not in exclude_cols]
    
    if len(feature_cols) == 0:
        raise ValueError("No feature columns found. Please check your dataframe columns.")
    
    # Extract features
    X = df[feature_cols].copy()
    
    # Extract XGBoost probabilities (this is our target)
    xgb_proba = df[xgb_proba_col].values
    
    # Create bin labels based on intervals
    # Assign each sample to a bin based on its interval
    unique_intervals = df[['proba_interval_start', 'proba_interval_end']].drop_duplicates().sort_values('proba_interval_start').reset_index(drop=True)
    
    # Create mapping from interval to bin number
    interval_to_bin = {}
    for idx, (start, end) in enumerate(unique_intervals.values):
        interval_to_bin[(start, end)] = idx + 1  # Bins numbered 1-10
    
    # Assign bin labels to each sample
    original_bin_labels = []
    for idx, row in df.iterrows():
        interval_key = (row['proba_interval_start'], row['proba_interval_end'])
        if interval_key in interval_to_bin:
            original_bin_labels.append(interval_to_bin[interval_key])
        else:
            # Find closest interval if exact match not found
            min_dist = float('inf')
            closest_bin = 1
            for (start, end), bin_num in interval_to_bin.items():
                mid = (start + end) / 2
                dist = abs(row[xgb_proba_col] - mid)
                if dist < min_dist:
                    min_dist = dist
                    closest_bin = bin_num
            original_bin_labels.append(closest_bin)
    
    original_bin_labels = np.array(original_bin_labels)
    
    # Train-test split (7:3)
    X_train, X_test, y_proba_train, y_proba_test, \
    bin_train, bin_test = train_test_split(
        X, xgb_proba, original_bin_labels,
        test_size=0.3, random_state=42
    )
    
    print(f"Training set size: {len(X_train)} ({len(X_train)/len(X)*100:.1f}%)")
    print(f"Test set size: {len(X_test)} ({len(X_test)/len(X)*100:.1f}%)")
    
    # Train Decision Tree Regressor to predict probabilities
    # Using parameters to balance accuracy and interpretability
    dt_regressor = DecisionTreeRegressor(
        max_depth=10,
        min_samples_split=20,
        min_samples_leaf=10,
        random_state=42
    )
    
    print("\nTraining surrogate decision tree...")
    dt_regressor.fit(X_train, y_proba_train)
    
    # Predict probabilities on test set
    y_pred_proba = dt_regressor.predict(X_test)
    
    # Clip predictions to [0, 1] range
    y_pred_proba = np.clip(y_pred_proba, 0, 1)
    
    # Convert predictions to bins using the same intervals
    def assign_bin(proba):
        """Assign bin based on probability value using the interval definitions."""
        for idx, (start, end) in enumerate(unique_intervals.values):
            if start <= proba <= end:
                return idx + 1
        # If outside all intervals, assign to closest bin
        if proba < unique_intervals['proba_interval_start'].min():
            return 1
        elif proba > unique_intervals['proba_interval_end'].max():
            return len(unique_intervals)
        else:
            # Find closest interval midpoint
            distances = []
            for start, end in unique_intervals.values:
                mid = (start + end) / 2
                distances.append(abs(proba - mid))
            return np.argmin(distances) + 1
    
    # Assign bins to predicted probabilities
    y_pred_bins = np.array([assign_bin(p) for p in y_pred_proba])
    
    # Evaluate probability approximation (regression metrics)
    mae_proba = mean_absolute_error(y_proba_test, y_pred_proba)
    rmse_proba = np.sqrt(mean_squared_error(y_proba_test, y_pred_proba))
    r2_proba = r2_score(y_proba_test, y_pred_proba)
    
    # Calculate additional metrics
    mape = np.mean(np.abs((y_proba_test - y_pred_proba) / (y_proba_test + 1e-8))) * 100
    
    # Evaluate bin classification accuracy
    bin_accuracy = accuracy_score(bin_test, y_pred_bins)
    bin_cm = confusion_matrix(bin_test, y_pred_bins)
    
    # Print results
    print("\n" + "=" * 70)
    print("SURROGATE DECISION TREE EVALUATION RESULTS")
    print("=" * 70)
    print(f"\nNumber of features: {len(feature_cols)}")
    print(f"Feature names: {feature_cols}")
    
    print("\n" + "-" * 70)
    print("PROBABILITY APPROXIMATION (XGBoost proba vs Tree proba)")
    print("-" * 70)
    print(f"Mean Absolute Error (MAE):        {mae_proba:.6f}")
    print(f"Root Mean Squared Error (RMSE):  {rmse_proba:.6f}")
    print(f"R² Score:                        {r2_proba:.6f}")
    print(f"Mean Absolute Percentage Error:  {mape:.2f}%")
    
    print("\n" + "-" * 70)
    print("BIN CLASSIFICATION ACCURACY")
    print("-" * 70)
    print(f"Overall Accuracy: {bin_accuracy:.4f} ({bin_accuracy*100:.2f}%)")
    
    print("\nConfusion Matrix (Rows = Actual bins, Columns = Predicted bins):")
    print("     ", end="")
    for i in range(1, len(unique_intervals) + 1):
        print(f"Bin{i:2d}", end="  ")
    print()
    for i, row in enumerate(bin_cm):
        print(f"Bin{i+1:2d} ", end="")
        for val in row:
            print(f"{val:5d}", end="  ")
        print()
    
    print("\nClassification Report:")
    print(classification_report(bin_test, y_pred_bins, 
                                target_names=[f'Bin {i+1}' for i in range(len(unique_intervals))],
                                zero_division=0))
    
    # Additional statistics
    print("\n" + "-" * 70)
    print("ADDITIONAL STATISTICS")
    print("-" * 70)
    print(f"XGBoost proba range: [{y_proba_test.min():.4f}, {y_proba_test.max():.4f}]")
    print(f"Tree proba range:    [{y_pred_proba.min():.4f}, {y_pred_proba.max():.4f}]")
    print(f"Mean XGBoost proba:  {y_proba_test.mean():.4f}")
    print(f"Mean Tree proba:     {y_pred_proba.mean():.4f}")
    
    # Store results
    results = {
        'model': dt_regressor,
        'feature_cols': feature_cols,
        'proba_metrics': {
            'mae': mae_proba,
            'rmse': rmse_proba,
            'r2': r2_proba,
            'mape': mape
        },
        'bin_metrics': {
            'accuracy': bin_accuracy,
            'confusion_matrix': bin_cm
        },
        'unique_intervals': unique_intervals.values,
        'X_test': X_test,
        'y_proba_test': y_proba_test,
        'y_pred_proba': y_pred_proba,
        'bin_test': bin_test,
        'y_pred_bins': y_pred_bins
    }
    
    return dt_regressor, results


if __name__ == "__main__":
    # Example usage:
    # Load your dataframe
    # df = pd.read_csv('your_data.csv')
    
    # Make sure your dataframe has these columns:
    # - Feature columns (any number)
    # - 'original_binary_target'
    # - 'xgboost_proba' (or specify different name)
    # - 'proba_interval_start'
    # - 'proba_interval_end'
    
    # Train the surrogate tree
    # dt_model, eval_results = train_surrogate_tree(df, xgb_proba_col='xgboost_proba')
    
    print("Surrogate Decision Tree Training Module")
    print("=" * 70)
    print("\nTo use this module:")
    print("1. Load your dataframe with columns: [features..., original_binary_target,")
    print("   xgboost_proba, proba_interval_start, proba_interval_end]")
    print("2. Call: dt_model, results = train_surrogate_tree(df)")
    print("3. The function will train the model and print evaluation results")
    print("\nExample:")
    print("  import pandas as pd")
    print("  df = pd.read_csv('your_data.csv')")
    print("  dt_model, results = train_surrogate_tree(df)")