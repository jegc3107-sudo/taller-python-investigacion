# Programa: Calculadora de compras
# Autor: Juan Esteban Giraldo
# Fecha: 2026-05-16


cantidad = int(input("¿Cuántos productos va a comprar? "))

total = 0
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    total += precio

if total > 100:
    descuento = total * 0.10
    total -= descuento
    print(f"Se aplicó un descuento de $ {descuento:.2f}")

print(f"El total a pagar es: $ {total:.2f}")
