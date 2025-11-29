# main.py

from utils import sumar, restar, multiplicar, dividir, potencia # <<-- Importa la nueva función

def mostrar_menu():
    print("\n--- Calculadora Básica ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia") # <<-- NUEVA OPCIÓN
    print("6. Salir")    # <<-- CAMBIÓ A 6

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "6": # <<-- AHORA SALE CON 6
            print("¡Hasta luego!")
            break

        # Se pide input solo si no es la opción de Salir
        try:
            a = float(input("Ingresa el primer número (o base): "))
            b = float(input("Ingresa el segundo número (o exponente): "))
        except ValueError:
            print("Error: Ingresa números válidos.")
            continue

        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            print("Resultado:", dividir(a, b))
        elif opcion == "5": # <<-- LÓGICA DE POTENCIA
            print("Resultado:", potencia(a, b))
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()