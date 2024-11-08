from scipy.optimize import linprog
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función objetivo (maximizar ganancias)
funcion_objetivo = [-10, -15, -20]  # Negativos porque linprog minimiza por defecto

# Definición de las restricciones
# Restricciones de capacidad de servidores, almacenamiento, computación y bases de datos
restricciones = [
    [1, 1, 1],   # S1 + C1 + B1 <= 500 (capacidad de servidores)
    [1, 0, 0],   # S1 <= 800 (recursos de almacenamiento)
    [0, 1, 0],   # C1 <= 200 (demanda de computación)
    [0, 0, 1]    # B1 <= 150 (demanda de bases de datos)
]

# Recursos disponibles para cada restricción
Disponibles = [500, 800, 200, 150]

# Límites para las variables S1, C1, B1 (todas >= 0)
limites_variables = [(0, None), (0, None), (0, None)]

# Resolviendo el problema de optimización
Resultado = linprog(c=funcion_objetivo, A_ub=restricciones, b_ub=Disponibles, bounds=limites_variables, method='highs')

# Verificando si hay una solución óptima
if Resultado.success:
    print('Solución Óptima Encontrada')
    
    S1, C1, B1 = Resultado.x
    print(f'Almacenamiento (S1): {round(S1)}')
    print(f'Computación (C1): {round(C1)}')
    print(f'Bases de Datos (B1): {round(B1)}')
    print(f'Ganancia Máxima: {round(-Resultado.fun)}')
else:
    print('No se pudo encontrar una solución óptima')

# Parte gráfica (Opcional, si quieres ver las restricciones y el área factible)
x1 = np.linspace(0, 500, 400)

# Restricciones gráficas (Capacidad, Computación y Bases de Datos)
r1_x2 = (500 - 1 * x1) / 1
r1_x2 = np.clip(r1_x2, 0, None)

r2_x2 = (800 - 1 * x1) / 1
r2_x2 = np.clip(r2_x2, 0, None)

r3_x2 = (200 - 0 * x1) / 1
r3_x2 = np.clip(r3_x2, 0, None)

r4_x2 = (150 - 0 * x1) / 1
r4_x2 = np.clip(r4_x2, 0, None)

# Graficando las restricciones
plt.plot(x1, r1_x2, label='Restricción 1: S1 + C1 + B1 ≤ 500', color='blue')
plt.plot(x1, r2_x2, label='Restricción 2: S1 ≤ 800', color='green')
plt.plot(x1, r3_x2, label='Restricción 3: C1 ≤ 200', color='red')
plt.plot(x1, r4_x2, label='Restricción 4: B1 ≤ 150', color='purple')

# Sombrear la región factible
plt.fill_between(x1, np.minimum(np.minimum(r1_x2, r2_x2), np.minimum(r3_x2, r4_x2)), color='gray', alpha=0.3)

# Graficar la función objetivo
z = -Resultado.fun  # Valor óptimo de la función objetivo
plt.plot(x1, (z - funcion_objetivo[0] * x1) / funcion_objetivo[1], label='Función objetivo', color='orange', linestyle='--')

# Solución óptima
plt.plot(S1, C1, 'ro', label=f'Solución óptima: ({round(S1)}, {round(C1)})')

# Ajustamos la gráfica
plt.xlim((0, 500))
plt.ylim((0, 200))  # Ajustamos los límites de la gráfica
plt.xlabel('S1: Almacenamiento')
plt.ylabel('C1: Computación')
plt.title('Región factible y función objetivo')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()
plt.grid(True)

# Mostramos la gráfica
plt.show()
