
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

