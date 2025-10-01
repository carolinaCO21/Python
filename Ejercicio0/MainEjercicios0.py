    

from Ejercicios0 import (
    isPar, ordenarNumeros, sumarNumeros, adivinaElNumero, aprenderAContar, factorial,
    isNumeroPrimo, imprimirTriagulo, numerosComprendidosEntre, isVocal, Calculadora
)

def ejercicio1():
    #1
    print("========================")
    print("Ejericio 1")
    print("Es par o impar?")
    valorIntroducido:int= int(input("introduce un número entero: "))
    #print(type(valorIntroducido))
    isPar(valorIntroducido)
def ejercicio2():
    #2
    print("========================")
    print("Ejericio 2")
    print("Introduce dos números número+ enter + número-> ordenaremos de menor a mayor")
    a: int = int(input("Número 1: "))
    b: int = int(input("Núemro 2 "))
    print("Resultado:")
    ordenarNumeros(a, b)

def ejercicio3():
    #3
    print("========================")
    print("Ejericio 3")
    numeros:str = input("Introduce una lista de números separados por comas: ")
    
    print(f"Resultado: {sumarNumeros(numeros)}")
    
def ejercicio4():
    #4
    print("========================")
    print("Ejericio 4")
    print("Adivina el número entre 1 y 100, -1 para rendirte4")
    adivinaElNumero()

def ejercicio5():
    #5
    print("========================")
    print("Ejericio 5")
    print("Contemos de 1 a N: Introduzca un número entero")
    numero:int= int(input())
    print("Contemos:")
    aprenderAContar(numero)
    print()

def ejercicio6():
    #6
    print("========================")
    print("Ejericio 6")
    print("Calcular el factorial: ")
    numero:int = int(input("Ingrese un entero > 0: "))
    print(f"El factorial es: {factorial(numero)}")

def ejercicio7():
    #7
    print("========================")
    print("Ejericio 7")
    print("Es número primo?")
    entrada:int = int(input("Introduzca un número entero >0: "))
    print(f"{entrada} es primo") if(isNumeroPrimo(entrada)) else print(f"{entrada} no es primo")

def ejercicio8():
    #8
    print("========================")
    print("Ejericio 8")
    print("Crear un triangulo N x N")
    dimension:int = int(input("Introduzca la dimension del triagulo: "))
    imprimirTriagulo(dimension)

def ejercicio9():
    #9
    print("========================")
    print("Ejericio 9_ Números comprendidos entre A y B")
    a:int = int(input("a:")) 
    b:int = int(input("b:"))
    numerosComprendidosEntre(a,b)

def ejercicio10():
    #10
    print("========================")
    print("Ejericio 10")
    print("MÁXIMO? Introduzca dos números enteros:")
    a:int = int(input("a: "))
    b:int = int(input("b: "))
    print(f"Máximo: {max(a,b)}")

def ejercicio11():
      #11
    print("========================")
    print("Ejericio 11")
    print("Es vocal? Introduzca una letra")
    letra:str = input("Letra: ")
    res:str= f"{letra} es vocal" if(isVocal(letra)) else f"{letra} no es vocal"
    print(res)


def ejercicio12():
    #12
    print("========================")
    print("Ejericio 11")
    """
    diccionario = {
    "+": lambda a, b: a + b
    }
    print(operaciones["+"](5, 3))  # 8
    en el caso:
    def suma(a,b) etc etc
    diccionario = {
    "+"= Clase.suma
    }
    print(operaciones["+"](5,3)) #8
    """


    while True:
        print("\n--- Calculadora Profesional ---")
        print("Operaciones disponibles: +, -, *, /, ^, raiz")
        print("Escriba 'salir' para terminar")

        op = input("Operación: ").strip().lower()
        if op == "salir":
            break

        try:
            if op == "raiz":
                x = float(input("Número: "))
                resultado = Calculadora.calcular(op, x)
            else:
                x = float(input("Número 1: "))
                y = float(input("Número 2: "))
                resultado = Calculadora.calcular(op, x, y)

            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


switch = {
    1: ejercicio1,
    2: ejercicio2,
    3: ejercicio3,
    4: ejercicio4,
    5: ejercicio5, 
    6: ejercicio6,
    7: ejercicio7,
    8: ejercicio8,
    9: ejercicio9,
    10: ejercicio10,
    11: ejercicio11,
    12: ejercicio12
}

def main():
    while True:
        print("""
        =============================
                MENÚ PRINCIPAL
        =============================
        1. Es par o impar?
        2. Ordenar dos números
        3. Sumar números hasta 0
        4. Adivina el número
        5. Aprender a contar
        6. Factorial
        7. Es número primo?
        8. Imprimir triángulo
        9. Números comprendidos entre A y B
        10. Máximo entre dos números
        11. Es vocal?
        12. Calculadora Profesional
        0. Salir
        =============================
        """)
        print("\nSeleccione el ejercicio a ejecutar (1-12) o 0 para salir:")
        opcion = int(input("Opción: "))
        
        if opcion == 0:
            print("Saliendo...")
            break
        
        funcion = switch.get(opcion)
        if funcion:
            funcion() 
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
