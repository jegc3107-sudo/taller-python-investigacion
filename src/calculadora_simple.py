#Programa: Calculadora Basica
#Autor: Juan Esteban Giraldo
#Fecha 2026-05-15
# Descripcion: Solicita dos numeros y permite realizar operaciones basicas

#=====================
#INGRESO DE DATOS
#=====================
num1 = float(input("Ingreasa Primer numero:  "))
num2 = float(input("Ingrese segundo numero: "))
print("\nMENÚ DE OPERACIONES")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion = input("Elija una opción (1-4): ")
#=====================
if opcion == '1':
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif opcion == '2':
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif opcion == '3':
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida.")
    