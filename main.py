# Tipos de comentarios

# Comentario de una sola linea

'''
    Comentario
    para
    distintas
    lineas
'''

print('Bienvenido a la introducion de python')

# Como definir variables

'''
    Id -> name
    tipo -> String
    valor -> MaestroShifu
'''

name = 'MaestroShifu'

# Por buenas practicas de maneja [Snake case]
last_name = 'ShifuEnterPrise'

# Variables numericas
num1 = 20
num2 = 5

result = num1 = num2

print(num1)
print(num2)
print(result)

# Manejo de cadenas

age = 23

print(f'Me llamo {name} {last_name} y tengo {age} años')

# Como hacer para repetir una cadena N veces

print(name * 5)

# Manejo de listas

list = ['Python', 'Django', 'React', 'Vue']

# Al poner negativo empieza en sentido contrario del array
print(list[-1])

# Modificar en un una posicion determinada
list[1] = 'Javascript'

# Agregar un nuevo elemento a su ultima posicion
list.append('Angular')

# Agregar un nuevo elemento en un indice determinado
list.insert(3, 'NodeJS')

print(list)

# Manejo de Tuplas
# Los datos de una tupla son inmutables

tupla = ('Python', 'Django', 'React', 'Vue')

print(tupla[0])
print(tupla[-1])

# Manejo de diccionarios -> Es igual a un objeto en JS

data = {'name': 'Maestro', 'last_name': 'Shifu', 'age': 23}

# Para agregar nuevas propiedades
data['city'] = 'Bogota'

# Para eliminar una propiedad
del data['age']

# Como saber cuantas propiedades tenemos
print(len(data))

print(data)
print(f'Mi nombre es {data["name"]} {data["last_name"]}')

# Entrada y salida de datos por consola
name_input = input('Introduce tu nombre:')
print(f'Nombre por consola: {name_input}')

# Cambiar el tipo de variable

# float()
# int()
# bool()
# str()

num_a = input('Primer numero: ')
num_b = input('Segundo numero: ')

print(int(num_a) + int(num_b))

# IF ELSE

age = input('Ingresa tu edad: ')

# Tambien existe un if not
if int(age) >= 18:
    print('Eres mayor a 18')
else:
    print('Eres menor de edad')

'''
Por practicas se recomiendo maximo 3 anidaciones

if conditional:
    ... code
elif conditional:
    ... code
else:
    ... code  
'''

# Bucles for

numbers = [1, 55, 88, 43, 4, 7, 9, 0, 22]

for num in numbers:
    print(num)

# Sirve para crear un array de n cantidad
arrayItems = range(0, 20)

for x in arrayItems:
    print(x)

# Bucles while

count = 1
while count <= 50:
    count = count + 1

# Manejo de clases y objetos
'''
class Coche:
    # Pass sirve para crear una clase vacia
    pass

# Asi se crea una instancia
coche_a = Coche()
'''

# Manejo de imports

from coche import Coche, CocheDeportivo

# Import dentro de carpetas
# from carpeta.coche import Coche, CocheDeportivo

coche_a = Coche()
coche_a.pintar('Azul')
coche_b = Coche('Seat', 'Negro')
coche_b.preder_apagar()
coche_b.velocidad(100)

coche_lujo = CocheDeportivo()
