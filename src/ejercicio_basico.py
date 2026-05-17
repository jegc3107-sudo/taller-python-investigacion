"""
Ejercicio Básico: Calculadora de Edad
Practica con variables, input, y operaciones básicas
"""
ANIO_ACTUAL = 2026
print("=== CALCULADORA DE EDAD ===")
nombre = input("Tu nombre: ")
anio_nacimiento = input("¿En qué año naciste? ")
anio_nacimiento = int(anio_nacimiento)
edad = ANIO_ACTUAL - anio_nacimiento
print(f"\nHola {nombre}, tienes {edad} años")
if edad >= 18:
 print("Eres mayor de edad")
else:
 print("Eres menor de edad")
 anos_faltantes = 18 - edad
 print(f"Te faltan {anos_faltantes} años para ser mayor de edad")