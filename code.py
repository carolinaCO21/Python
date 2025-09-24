
#  BUCLES

edad = 0
while edad < 10:
    edad+=1
    print(edad)

# LAS CADENAS FUNCIONAN COMO LISTAS
print("foreach")
lista = [1,3,4,5,6,7]
for valor in lista:
    print(valor)



#métodos
print("Métodos")
def nombreFuncion(param1, param2:int):
    return param1 + param2


print(nombreFuncion("a","b"))
print(nombreFuncion(2,2))

"""
1.-Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.
2.-Pedir dos números y mostrarlos ordenados de menor a mayor.
3.-Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.
4.-Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, según sea mayor o menor con respecto al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).
5.-Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.
6.-Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.
7.-Realiza un programa que pida un número entero positivo y nos diga si es primo o no.
8.-Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
   *
  * *
 * * *
* * * *
9.-Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. Desde el método main() lee los dos números enteros, los cuales deben introducirlos el usuario, y pásalos como parámetros de entrada de la función.
10.-Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.
11.-Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de entrada corresponde con una vocal.
12.-Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y qué operación se desea realizar con ellos. Las operaciones disponibles son sumar, restar, multiplicar o dividir. Estas se especifican mediante un número: 1 para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división. La función devolverá el resultado de la operación mediante un número real.



"""