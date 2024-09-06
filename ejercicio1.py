import sympy as sp

# Definir la variable y la función
x = sp.symbols('x')
f = 25*x**3 - 6*x**2 + 7*x - 88

# Punto base
x0 = 1

# Valor a estimar
x_val = 3

# Calcular las derivadas
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)
f_triple_prime = sp.diff(f_double_prime, x)

# Evaluar la función y sus derivadas en el punto base
f_x0 = f.subs(x, x0)
f_prime_x0 = f_prime.subs(x, x0)
f_double_prime_x0 = f_double_prime.subs(x, x0)
f_triple_prime_x0 = f_triple_prime.subs(x, x0)

# Calcular los términos de la serie de Taylor
t0 = f_x0
t1 = f_prime_x0 * (x_val - x0)
t2 = f_double_prime_x0 * (x_val - x0)**2 / 2
t3 = f_triple_prime_x0 * (x_val - x0)**3 / 6

# Estimar f(3) usando la serie de Taylor
taylor_approx = t0 + t1 + t2 + t3
print(f"Estimación de f(3) usando la serie de Taylor: {taylor_approx:.6f}")

# Calcular el valor verdadero de f(3)
true_value = f.subs(x, x_val)
print(f"Valor verdadero de f(3): {true_value:.6f}")

# Calcular el error relativo porcentual verdadero para cada aproximación
def relative_error(true_value, approx_value):
    return abs((true_value - approx_value) / true_value) * 100

# Aproximaciones parciales
approximations = [t0, t0 + t1, t0 + t1 + t2, t0 + t1 + t2 + t3]

# Calcular y mostrar los errores relativos porcentuales verdaderos
for i, approx in enumerate(approximations):
    error = relative_error(true_value, approx)
    print(f"Aproximación de orden {i}: {approx:.6f}, Error relativo porcentual verdadero: {error:.6f}%")

# Análisis de resultados
print("\nAnálisis de resultados:")
print("A medida que se agregan más términos de la serie de Taylor, la aproximación se vuelve más precisa.")
print("El error relativo porcentual verdadero disminuye con cada término adicional, lo que indica una mejor aproximación.")