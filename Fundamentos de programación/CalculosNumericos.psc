Algoritmo CalculosNumericos
    Definir X, N, cuadrado, cubo, raizCuadrada, potencia Como Real
    
    // Leer el número X y el exponente N
    Escribir "Ingrese un número entero X:"
    Leer X
    Escribir "Ingrese el exponente N para la potencia:"
    Leer N
	
    // Calcular el cuadrado, cubo, raíz cuadrada y potencia
    cuadrado <- X ^ 2
    cubo <- X ^ 3
    raizCuadrada <- raiz(X)
    potencia <- X ^ N
	
    // Imprimir los resultados
    Escribir "El cuadrado de ", X, " es: ", cuadrado
    Escribir "El cubo de ", X, " es: ", cubo
    Escribir "La raíz cuadrada de ", X, " es: ", raizCuadrada
    Escribir X, " elevado a la potencia ", N, " es: ", potencia
FinAlgoritmo



