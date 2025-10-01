import random
from typing import Union
import math

"""
Función que retorna múltiples tipos (Union):
from typing import Union

def nombre_función(...) -> Union[Tipo1, Tipo2, ...]:
    ...
    return algo  # puede ser Tipo1 o Tipo2
"""
"""
1.Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.

2.Pedir dos números y mostrarlos ordenados de menor a mayor.

3.Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.

4.Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, según sea mayor o menor con respecto al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1)

5.Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.

6.Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.

7.Realiza un programa que pida un número entero positivo y nos diga si es primo o no.

8.Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
*
* *
* * *
* * * *

9.Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. Desde el método main() lee los dos números enteros, los cuales deben introducirlos el usuario, y pásalos como parámetros de entrada de la función.

10.Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.

11.Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de entrada corresponde con una vocal.

12.Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y qué operación se desea realizar con ellos. Las operaciones disponibles son sumar, restar, multiplicar o dividir. Estas se especifican mediante un número: 1 para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división. La función devolverá el resultado de la operación mediante un número real.
"""

#1
def isPar(valorIntroducido:int) -> None:
    res: str = f"{valorIntroducido} es par" if (int(valorIntroducido) % 2 == 0 ) else f"{valorIntroducido} es impar"
    print(res)

#2
def ordenarNumeros (a: int, b:int) -> None:
    print(f"{b} {a}") if (a>b)  else  print(f"{a} {b}")

#3
def sumarNumeros(numerosS:int) -> int:
    lista_numeros = [int(num.strip()) for num in numerosS.split(",")]
    return sum(lista_numeros)

#4
def adivinaElNumero(entrada:input) -> None:
   import random

def adivinaElNumero() -> None:
    num:int = random.randint(1, 100)
    print(f"debug: {num}")

    while True:
        entrada = input("Introduce un número (-1 para rendirte): ")

        try:
            numero:int = int(entrada)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if numero == num:
            print(f"¡Has ganado! El número era: {num}")
            break
        elif numero == -1:
            print("Te has rendido.")
            break
        elif numero > num:
            print("El número es menor.")
        else:
            print("El número es mayor.")

def ejercicio4():
    print("========================")
    print("Ejercicio 4")
    print("Adivina el número entre 1 y 100, -1 para rendirte")
    adivinaElNumero()


#5
def aprenderAContar(numero:int)-> None:
    for i in range(1,numero+1):
        print(f"{i} ", end=" ")

#6
def factorial(numero:int)-> int:
    if(numero == 0 or numero == 1):
        return 1
    elif(numero >1):
        return numero*factorial(numero-1)

#7
def isNumeroPrimo(num:int)-> bool:
    #Si ningún número entre 2 y √num lo divide exactamente → es primo, porque 1 y él mismo son los únicos divisores.
    if(num <2):
        return False
    rango:float= int(math.sqrt(num))
    for n in range(2, rango+1):
        if(num% n == 0):
            return False
    return True

#8
def imprimirTriagulo(n:int)-> None:
    for i in range(1,n+1):
        print(" " * (n - i) + "* " * i)
    """
    def imprimirTriangulo(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(i):          # igual j<i en java
            print("*", end="")
        print()
    """

#9
def numerosComprendidosEntre(a:int, b:int):
    inicio: int = a+1
    fin:int=  b
    if(b-a== 1):
        print("No hay números")
    else:
        for i in range(inicio, fin):
            if(i < fin):
                print(f"{i}, ", end="")
            else:
                print(f"{i} ")
    """
    def numeros_comprendidos_entre(a: int, b: int):
    numeros = list(range(a + 1, b))
    if not numeros:
        print("No hay números")
    else:
        print(", ".join(str(num) for num in numeros))
    """

#10
def max(a:int, b:int) -> int:
    res:int = a if(a>b) else b
    return res

#11
def isVocal(letra:str)-> bool:
    return len(letra)==1 and letra.isalpha() and letra.lower() in "aeiou"

#12
class Calculadora:
    operaciones = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        #generador como list comphrension en sintaxis pero mas bien como un suplier , tienes que iterar
        """
        gen = (x**2 for x in range(5))
        print(next(gen))  # 0
        print(next(gen))  # 1
        """
        "/": lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ValueError("No se puede dividir entre cero")),
        "^": lambda x, y: x ** y,
        "raiz": lambda x: math.sqrt(x) if x >= 0 else (_ for _ in ()).throw(ValueError("No se puede calcular raíz de un número negativo"))
    }

    #empaqueta y desempaqueta argumentos. *args -> tupla (1,2,3) que se desempaqueta
    #print(a[..., 0])  # toma el primer elemento de la última dimensión
    @staticmethod
    def calcular(op: str, *valores: float) -> float:
        if op not in Calculadora.operaciones:
            raise ValueError(f"Operación '{op}' no válida")
        return Calculadora.operaciones[op](*valores)
