import random
from typing import Union


"""
Función que retorna múltiples tipos (Union):
from typing import Union

def nombre_función(...) -> Union[Tipo1, Tipo2, ...]:
    ...
    return algo  # puede ser Tipo1 o Tipo2

"""
#1
def isPar() -> None:
    print("Es par o impar?")
    valorIntroducido:str = input("introduce un número: ")
    #print(type(valorIntroducido))
    res: str = "Es par" if (int(valorIntroducido) % 2 == 0 ) else "Es impar"
    print(res)



#2
def ordenarNumeros () -> None:
    print("Introduce dos números -> ordenaremos de menor a mayor")
    a: int = int(input())
    b: int = int(input())

    res: str = "Resultado: "
    print(f"{res} {a} {b}") if (a>b)  else  print(f"{res} {b} {a}") 


#3

def sumarNumeros() -> int:
    print("Introduce una lista de números separados por comas")
    numeros:str = input() 
    lista = numeros.strip().split(",")
    #(list comprehension):  sintaxis -> [expresión for elemento in iterable]
    """
    1.-Recorre cada elemento en el iterable.

    2.-Aplica la expresión al elemento.

    3.-Guarda el resultado en una nueva lista automáticamente.
    """

    #elimino los espacios con 
    lista = [int(val.strip()) for val in lista]
    
    return sum(lista)
    #print(type(lista))
    print(lista)


#4

def adivinaElNumero () -> None:

    num:int = random.randint(1,100)
    



def main():
    print("Este es el programa principal")
    #1
    isPar()
    #2
    ordenarNumeros()
    #3
    print(sumarNumeros())
    #4

if __name__ == "__main__":
    main()

