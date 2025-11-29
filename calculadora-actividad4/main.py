from utils import sumar, restar, multiplicar, dividir

def mostrar_menu():
    print("\n--- Calculadora Básica ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            print("Resultado:", dividir(a, b))
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
# utils.py

import math # <<-- ¡IMPORTANTE!

# Funciones de Operaciones Básicas
def sumar(a, b):
    # ... (código existente)

# ... (otras funciones)

# Función de Raíz Cuadrada (HU-02)
def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz de número negativo"
    return math.sqrt(a)