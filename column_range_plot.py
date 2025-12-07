import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    num_cols = A.shape[1]
    col_ranges = []
    
    for i in range(num_cols):
        col = A[:, i]
        min_val = np.min(col)
        max_val = np.max(col)
        col_ranges.append(max_val - min_val)
    
    col_ranges = np.array(col_ranges)
    
    plt.bar(range(num_cols), col_ranges)
    plt.savefig(filename)

    return col_ranges