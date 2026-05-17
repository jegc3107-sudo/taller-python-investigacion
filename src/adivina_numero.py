# Programa: Adivina el número secreto
# Autor: Juan Esteban Giraldo
# Fecha: 2026-05-16


NUMERO_SECRETO = 42


intentos = 0
MAX_INTENTOS = 5
adivinado = False


while intentos < MAX_INTENTOS and not adivinado:
    
    numero = int(input(f"Intento {intentos+1}/{MAX_INTENTOS} - Adivina el número: "))
    intentos += 1

    if numero == NUMERO_SECRETO:
        print("🎉 ¡Felicitaciones! Adivinaste el número secreto.")
        adivinado = True
    elif numero < NUMERO_SECRETO:
        print("El número secreto es MAYOR.")
    else:
        print("El número secreto es MENOR.")


if not adivinado:
    print(f" Se acabaron los intentos. El número secreto era {NUMERO_SECRETO}.")
