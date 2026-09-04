import numpy as np
import pandas as pd

def recursive_bin(
    x: np.ndarray, 
    max_bins: int = 10, 
    min_abs_samples: int = 30, 
    min_pct_samples: float = 0.01
) -> np.ndarray:
    """
    Recursively bins 1D numerical data by isolating point-mass spikes and 
    adaptively splitting continuous regions.
    
    Parameters:
    -----------
    x : 1D numpy array
        Target numeric variable to bin.
    max_bins : int, default=10
        Maximum total number of discrete bins to generate.
    min_abs_samples : int, default=30
        Absolute lower bound on samples required inside a node to allow a split.
    min_pct_samples : float, default=0.01 (1%)
        Percentage lower bound of N_total required inside a node to allow a split.
    """
    x = np.asarray(x)
    n_total = len(x)
    
    # Dual-constraint minimum sample threshold
    pct_count = int(np.ceil(n_total * min_pct_samples))
    effective_min_samples = max(2, min_abs_samples, pct_count)
    
    bin_assignments = np.zeros(n_total, dtype=int)
    current_bin_id = 0

    def _split_node(indices, bins_remaining):
        nonlocal current_bin_id
        
        if len(indices) == 0:
            return
            
        sub_x = x[indices]
        vals, counts = np.unique(sub_x, return_counts=True)
        
        # Base Case 1: Pure node, no bin budget, or below dual sample threshold
        if len(vals) == 1 or bins_remaining <= 1 or len(indices) < effective_min_samples:
            bin_assignments[indices] = current_bin_id
            current_bin_id += 1
            return

        # Base Case 2: Detect point-mass spike (isolates dominant single value)
        top_idx = np.argmax(counts)
        top_freq = counts[top_idx] / len(indices)
        
        if top_freq >= (1.0 / max_bins):
            dominant_val = vals[top_idx]
            spike_mask = (sub_x == dominant_val)
            
            # Isolate spike into dedicated bin
            bin_assignments[indices[spike_mask]] = current_bin_id
            current_bin_id += 1
            
            # Recurse on remaining data
            remainder_indices = indices[~spike_mask]
            _split_node(remainder_indices, bins_remaining - 1)
        else:
            # Step: Median split for continuous distribution
            median_val = np.median(sub_x)
            left_mask = (sub_x <= median_val)
            right_mask = ~left_mask
            
            if not np.any(left_mask) or not np.any(right_mask):
                bin_assignments[indices] = current_bin_id
                current_bin_id += 1
                return

            left_bins = bins_remaining // 2
            right_bins = bins_remaining - left_bins
            
            _split_node(indices[left_mask], left_bins)
            _split_node(indices[right_mask], right_bins)

    _split_node(np.arange(n_total), max_bins)
    return bin_assignments
