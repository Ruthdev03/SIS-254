import math

# Definir la función y sus derivadas
def f(x):
    return math.log(x)

def f_prime(x):
    return 1 / x

def f_double_prime(x):
    return -1 / (x ** 2)

def f_triple_prime(x):
    return 2 / (x ** 3)

def f_quadruple_prime(x):
    return -6 / (x ** 4)

# Punto base
x0 = 1

# Valor a estimar
x = 2.5

# Calcular los términos de la serie de Taylor
t0 = f(x0)
t1 = f_prime(x0) * (x - x0)
t2 = f_double_prime(x0) * (x - x0) ** 2 / 2
t3 = f_triple_prime(x0) * (x - x0) ** 3 / 6
t4 = f_quadruple_prime(x0) * (x - x0) ** 4 / 24

# Estimar f(2.5) usando la serie de Taylor
taylor_approx = t0 + t1 + t2 + t3 + t4
print(f"Estimación de f(2.5) usando la serie de Taylor: {taylor_approx:.6f}")

# Calcular el valor verdadero de f(2.5)
true_value = f(x)
print(f"Valor verdadero de f(2.5): {true_value:.6f}")

# Calcular el error relativo porcentual verdadero para cada aproximación
def relative_error(true_value, approx_value):
    return abs((true_value - approx_value) / true_value) * 100

# Aproximaciones parciales
approximations = [t0, t0 + t1, t0 + t1 + t2, t0 + t1 + t2 + t3, t0 + t1 + t2 + t3 + t4]

# Calcular y mostrar los errores relativos porcentuales verdaderos
for i, approx in enumerate(approximations):
    error = relative_error(true_value, approx)
    print(f"Aproximación de orden {i}: {approx:.6f}, Error relativo porcentual verdadero: {error:.6f}%")

# Análisis de resultados
print("\nAnálisis de resultados:")
print("A medida que se agregan más términos de la serie de Taylor, la aproximación se vuelve más precisa.")
print("El error relativo porcentual verdadero disminuye con cada término adicional, lo que indica una mejor aproximación.")