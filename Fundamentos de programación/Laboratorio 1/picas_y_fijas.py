import random

def generar_numero_clave():
    # Genera un número de 4 dígitos sin repetir dígitos
    digitos = list(range(10))
    random.shuffle(digitos)
    numero_clave = ''.join(str(digitos[i]) for i in range(4))
    return numero_clave

def contar_picas_y_fijas(numero_clave, intento):
    picas = 0
    fijas = 0
    for i in range(4):
        if intento[i] == numero_clave[i]:
            fijas += 1
        elif intento[i] in numero_clave:
            picas += 1
    return picas, fijas

def jugar():
    numero_clave = generar_numero_clave()
    intentos = 0
    max_intentos = 12

    print("¡Bienvenido al juego de Picas y Fijas!")
    print("Intenta adivinar el número de 4 dígitos sin repetir cifras.")

    while intentos < max_intentos:
        intento = input("Ingresa tu intento de 4 dígitos: ")
        
        # Validar entrada del usuario
        if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
            print("El número debe tener 4 dígitos únicos. Inténtalo de nuevo.")
            continue

        intentos += 1
        picas, fijas = contar_picas_y_fijas(numero_clave, intento)

        if fijas == 4:
            print(f"¡Felicidades! Adivinaste el número {numero_clave} en {intentos} intentos.")
            if intentos <= 2:
                print("Excelente, eres un maestro, estás fuera del alcance de los demás.")
            elif intentos <= 4:
                print("Muy bueno, puedes ser un gran competidor.")
            elif intentos <= 8:
                print("Bien, estás progresando, debes buscar tus límites.")
            elif intentos <= 10:
                print("Regular, aún es largo el camino por recorrer.")
            return

        print(f"Intento #{intentos}: {picas} picas, {fijas} fijas")

    # Si no ha adivinado después de 12 intentos
    print(f"Lo siento, no lograste adivinar el número. El número era {numero_clave}.")
    print("Mal, este juego no es para ti.")

# Ejecuta el juego
jugar()