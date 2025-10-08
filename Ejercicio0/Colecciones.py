import random, string
"""
1.-Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 

2.-Crea un programa que pida diez números reales por teclado, los almacene en una lista, y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.

3.-Realiza un programa que pida 8 números enteros y los almacene en una lista. A continuación, recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.

4.-Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.

5.-Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10. Luego pedirá un valor N y mostrará cuántas veces aparece N. 


6.-Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de cada palabra en el texto.


7.-Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario. La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. Crea un menú para las distintas opciones e implementa una función para cada opción.


8.-Diseña un programa que registre las ventas de una tienda en un diccionario, donde las claves son los nombres de los productos y los valores son las cantidades vendidas. El programa debe permitir al usuario agregar nuevas ventas y calcular el total de ventas para un producto específico. Implementa un menú con ambas opciones. 


9.-Crea un diccionario donde las claves son las letras del abecedario y los valores, la puntuación para cada letra, como en el Scrabble. El programa le pedirá una palabra al usuario y se mostrará por pantalla la puntuación que tiene la palabra en total.

10.-Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:

conjunto 1:
e
i
k
m
p
q
r
s
t
u
v
conjunto 2: 
p
v
i
u
m
t
e
r
k
q
s

El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. Para ello, cada vez que encuentre en la frase una letra del conjunto 1 la sustituirá por su correspondiente en el conjunto 2.

"""

#1 y 5

def listaEnterosAleatorios(inicio:int, fin:int) -> list[int]:
    listaEnterosAleatorios = [random.randint(inicio,fin) for i in range(10)]
    return listaEnterosAleatorios


#2
def mostrarMaxMin(lista_numeros:list[int]) -> None:
    numeros = lista_numeros
    print(f"Máximo: {max(numeros)}")
    print(f"Mínimo: {min(numeros)}")

#3
def esPar(lista_numeros:list[int]) -> None:
    for num in lista_numeros:
        f"{num} es par" if (num %2 == 0) else f"{num} es impar"
    

#4
def ordenarNumeros (lista_numeros:list[int]):
    lista_numeros.sort(reverse=True)
    return lista_numeros


#6
def contarPalabras(texto:str) -> dict[str,int]:
    palabras = texto.split()
    palabras = [palabra.strip(string.punctuation).lower() for palabra in palabras] #limpamos puntuación hola, etc
    palabras = [palabra for palabra in palabras if palabra.isalpha()]
    diccionario_frecuencia:dict[str,int] ={}
    for palabra in palabras:
        if palabra in diccionario_frecuencia:
            diccionario_frecuencia[palabra] += 1
        else:
            diccionario_frecuencia[palabra] = 1 
    return diccionario_frecuencia

#7

