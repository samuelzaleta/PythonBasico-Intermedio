print("hola, mundo")
print("La Witsi Witsi Araña subió a su telaraña.")
print()
print("Vino la lluvia y se la llevó.")
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")
print("La Witsi Witsi Arañar" , "subió" , "a su telaraña.")
print("Mi nombre es", "Python.")
print("Monty Python.")
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("2")
print(2)
print(0o123)
print(0x123)
print(0.0000000000000000000001)
print("Me gusta \"Monty Python\"")
print('Me gusta "Monty Python"')
print(True > False)
print(True < False)
print('"Estoy"')
print('""aprendiendo""')
print('""\"Python\"""')
print(2+2)
print(2 ** 3) #2^3
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print(2 * 3) #2 * 3 = 6
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print(6 // 3) # Un símbolo de // (doble diagonal) es un operador de división entera.
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print(6 // 4)
print(6. // 4)
print(-6 // 4)
print(6. // -4)
print(14 % 4) #Modulo
print(-4 + 4)
print(-4. + 8)
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(2 + 3 * 5) #Seguramente recordaras que primero se debe multiplicar 3 por 5, mantener el 15 en tu memoria y después sumar el 2, dando como resultado el 17.
print(9 % 6 % 2) #De izquierda a derecha: primero 9 % 6 da como resultado 3, y entonces 3 % 2 da como resultado 1
print(2 ** 2 ** 3)
# de izquierda a derecha
print(2*2)
print(4**3)
# de derecha a izquierda
print(2**3)
print(2**8)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print(2 * 3 % 5)
print((2**4), (2*4.), (2*4))
print((-2/4), (2/4), (2//4), (-2//4))
print((2%-4), (2%4), (2**3**2)) #2**3**2 512 = 2**9
var = 1
print(var)
balance_cuenta = 1000.0
nombreCliente = 'John Doe'
print(var, balance_cuenta, nombreCliente)
print(var)
var = var + 1
print(var)
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5 # (a^2 + b^2)^1/2
print("c =", c)
nombre ='juan'
nombre1 ='maria'
nombre2 ='adan'
manzanasJuan = 3
manzanasMaria = 7
manzanasAdan = 8
totalManzanas = manzanasJuan + manzanasMaria + manzanasAdan
print(totalManzanas)
print(nombre , ' tiene ', manzanasJuan)
print(nombre1, ' tiene ', manzanasMaria)
print(nombre2, ' tiene ', manzanasAdan)

kilometros = 12.25
millas = 7.38

millas_a_kilometros = 0.621371
kilometros_a_millas = 1601

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")

# codifica aquí tus datos de prueba.
x = 1
# escribe tu código aquí.
y = ((3*x)**3) - ((2*x)**2) + (3*x) -1
print("y =", y)

a = 2 # numero de horas
segundos = 3600 # número de segundos en una hora

print("Horas: ", a) #imprime el numero de horas
print("Segundos en horas: ", a * segundos) # se imprime el numero de segundos en determinado numero de horas
#algo = int(input("Inserta un número: "))
#resultado = algo ** 2.0
#print(algo, "al cuadrado es ", resultado)
#algo = float(input("Inserta un número: "))
#resultado = algo ** 2.0
#print(algo, "al cuadrado es", resultado)

#cateto_a = float(input("Inserta la longitud del primer cateto: "))
#cateto_b = float(input("Inserta la longitud del segundo cateto "))
#hipo = (cateto_a**2 + cateto_b**2) ** .5
#print("La longitud de la hipotenusa es: ", hipo)
'''
nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")
'''
print('samuel' *3)
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
# ingresa un valor flotante para la variable a aquí
var1  =1.0
# ingresa un valor flotante para la variable b aquí
var2 =2.0
# muestra el resultado de la suma aquí
sumar = var1 + var2
print(sumar)
# muestra el resultado de la resta aquí
resta = var1 - var2
print(resta)
# muestra el resultado de la multiplicación aquí
multiplicacion = var1 * var2
print(multiplicacion)
# muestra el resultado de la división aquí
division = var1/var2
print(division)

print("\n¡Eso es todo, amigos!")
'''
x = float(input("Ingresa el valor para x: "))

# coloca tu código aquí
y =1/(x +(1/(x +1/(x + 1/x))))
print("y =", y)
'''
print(123 + 0.0)
lst =[1,2]
for v in range(2):
    lst.insert(-1,lst[v])
print(lst)
print(1//2)
z =0
y = 10
x = y < z and z > y or y > z and z <y
print("c ", x)
lis =[x *x for x in range(5)]
def func3(lis):
    del lis[lis[2]]
    return  lis
print(func3(lis))
x = 2.0
y = 4.0
print(y **(1/x))
dct ={'uno':'dos','tres':'uno','dos':'tres'}
v =dct['tres']
for k in range(len(dct)):
    v =dct[v]
print(v)
list = [i for i in range(-1,2)]
print(list)
def g(x,y):
    if x ==y:
        return x
    else:
        return g(x, y-1)
print("add",g(0,3))
dct ={}
dct[1]={1,2}
dct[2]={2,1}
for x in dct.keys():
    print(dct[x][1], end ="")