'''
Python conoce varios tipos de datos compuestos , utilizados para agrupar otros valores. La más versátil es la lista ,
que se puede escribir como una lista de valores (elementos) separados por comas entre corchetes.
Las listas pueden contener elementos de diferentes tipos, pero generalmente todos los elementos tienen el mismo tipo.
'''
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:]) # slicing devuelve una nueva lista
print(squares[:])
print(squares + [36, 49, 64, 81, 100])
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)
print(cubes)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
letters = ['a', 'b', 'c', 'd']
cont =len(letters)
print(cont)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x[0])
print(x[0][1])
