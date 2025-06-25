import numpy as np

# Coefficient matrix A
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

# Constants on the right-hand side (B)
B = np.array([8, -11, -3])

# Solve the system
solution = np.linalg.solve(A, B)

# Display the result
print("Solution (x, y, z):", solution)
