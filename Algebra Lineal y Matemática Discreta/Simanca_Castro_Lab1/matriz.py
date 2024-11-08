import numpy as np

def eliminacion_gaussiana_ppe(A, b):
    n = len(A)
    # Matriz extendida
    Ab = np.hstack([A, b.reshape(-1, 1)])  # Agregar la columna del vector b a la matriz A
    
    # Vector de escala
    escala = np.max(np.abs(A), axis=1)

    for i in range(n-1):
        # Pivotaje parcial escalado
        razones = np.abs(Ab[i:n, i]) / escala[i:n]
        pivot = np.argmax(razones) + i

        if pivot != i:
            # Intercambio de filas
            Ab[[i, pivot], :] = Ab[[pivot, i], :]
            escala[[i, pivot]] = escala[[pivot, i]]

        # Eliminación
        for j in range(i+1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] = Ab[j, i:] - factor * Ab[i, i:]
    
    # Devolver la matriz triangular superior y el vector b modificado
    return Ab[:, :-1], Ab[:, -1]

def sustitucion_regresiva(U, b):
    n = len(b)
    x = np.zeros(n)
    
    # Resolver desde la última ecuación hacia atrás
    for i in range(n-1, -1, -1):
        suma = np.dot(U[i, i+1:], x[i+1:])
        x[i] = (b[i] - suma) / U[i, i]
    
    return x

# Ejemplo de uso
A = np.array([[6.0, -2.0, 2.0, 4.0],
              [12.0, -8.0, 6.0, 10.0],
              [3.0, -13.0, 9.0, 3.0],
              [-6.0, 4.0, 1.0, -18.0]])

b = np.array([ 16.0, 26.0, -19.0, -34.0])

# Limitar la impresión de decimales a 2
np.set_printoptions(precision=2, suppress=True)

# Imprimir la matriz original y el vector b
print("Matriz original A:")
print(A)
print("Vector original b:")
print(b)

# Paso 1: Obtener la matriz triangular superior y el vector modificado
A_triangular, b_modificada = eliminacion_gaussiana_ppe(A, b)

print("\nMatriz triangular superior A:")
print(A_triangular)
print("Vector b modificado:")
print(b_modificada)

# Paso 2: Sustitución regresiva para obtener los valores de x
x = sustitucion_regresiva(A_triangular, b_modificada)

print("\nSolución del sistema (x1, x2, x3, x4):")
print(x)