import numpy as np
requerimientos = np.array([4800, 5810, 5690])
A = np.array([[52, 30, 18],   # Cantera 1
              [20, 50, 30],   # Cantera 2
              [25, 20, 55]])  # Cantera 3
x = np.zeros(3)
def jacobi(A, b, x, iterations=25):
    n = len(b)
    for _ in range(iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        x = x_new
    return x
cantidades_transportadas = jacobi(A, requerimientos, x)
print("Cantidades a transportar:", cantidades_transportadas)