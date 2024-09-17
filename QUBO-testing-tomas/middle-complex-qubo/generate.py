import numpy as np

# d - matrix size
# k - size of the optimal solution
def qubo_matrix(d, k):
    # Top left k-size submatrix is non-positive
    # Other submatrices are non-negative
    # Hence, optimal solution is to pick the first k rows/columns
    A11 = -np.random.rand(k, k)
    A12 = np.random.rand(k, d - k)
    A21 = np.random.rand(d - k, k)
    A22 = np.random.rand(d - k, d - k)
    
    A = np.vstack([
        np.hstack([A11, A12]),
        np.hstack([A21, A22]),
    ])
    x_opt = np.hstack([np.ones(k), np.zeros(d-k)])

    # Shuffle rows and columns in the same way
    inds = np.arange(d)
    np.random.shuffle(inds)
    A = A[:, inds][inds, :]
    x_opt = x_opt[inds]
    
    return A, x_opt
