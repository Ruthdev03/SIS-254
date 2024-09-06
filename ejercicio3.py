def nanning_formula(n, B, H, S):
    return (5 * B * (1 + 3 * n * B * H) ** 0.2) / (2 * S ** 0.5)

def calculate_sensitivity(n, B, H, S, delta_n, delta_S):
    Q_initial = nanning_formula(n, B, H, S)
    delta_Q_n = nanning_formula(n + delta_n, B, H, S) - Q_initial
    delta_Q_S = nanning_formula(n, B, H, S + delta_S) - Q_initial
    sensitivity_n = delta_Q_n / delta_n
    sensitivity_S = delta_Q_S / delta_S
    return sensitivity_n, sensitivity_S

# Datos del problema
n = 0.03  # coeficiente de rugosidad
B = 20.0  # ancho
H = 0.3   # profundidad
S = 0.0003  # pendiente
delta_n = 0.03 * 0.1  # 10% de variación de la rugosidad
delta_S = 0.0003 * 0.1  # 10% de variación de la pendiente

# Cálculo del flujo inicial
Q_initial = nanning_formula(n, B, H, S)
print(f"Flujo inicial (Q): {Q_initial:.4f} m³/s")

# Cálculo de la sensibilidad
sensitivity_n, sensitivity_S = calculate_sensitivity(n, B, H, S, delta_n, delta_S)
print(f"Sensibilidad respecto a la rugosidad (n): {sensitivity_n:.4f}")
print(f"Sensibilidad respecto a la pendiente (S): {sensitivity_S:.4f}")

# Determinar cuál factor debería medirse con mayor precisión
if abs(sensitivity_n) > abs(sensitivity_S):
    print("Se debería intentar medir la rugosidad (n) con mayor precisión.")
else:
    print("Se debería intentar medir la pendiente (S) con mayor precisión.")