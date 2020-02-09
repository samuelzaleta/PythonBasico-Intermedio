'''*
** Numeros
'''
'''interprete como calculadora'''
print( 2 + 2) # operador de suma es +
print((50 - 5*6)/4) # operador de multipliación * , operador de resta -
print(17/3) #operador de división /
print(17//3) #trucar residuo de división
print(17 % 3) #Operación módulo que regresa el residuo de realizar una división entera entre dos números %
print(2 ** 9) #operador de potencia **
width = 20
height = 5 * 9
print(width * height)
print( 4 * 3.75 -1) #Hay soporte completo para coma flotante; Los operadores con operandos de tipo mixto convierten el operando entero en coma flotante
tax = 12.5/1000
price = 100
print(price*tax)

'''
Devuelve el número de bits necesarios para representar un entero en binario, excluyendo el signo y los ceros a la izquierda:
>>> n = -37
>>> bin(n)
'-0b100101'
>>> n.bit_length()
6
'''
'''
Operaciones en secuencia común
[x in s] -> True si un elemento de s es igual a x , de lo contrarioFalse
[x not in s] -> False si un elemento de s es igual a x , de lo contrarioTrue
min(s) -> elemento más pequeño de s
max(s) -> elemento más grande de s
s.index(x[, i[, j]]) ->índice de la primera aparición de x en s (en o después del índice i y antes del índice j )
s.count(x) ->
'''