'''* Cadenas
**Python también puede manipular cadenas, que se pueden expresar de varias maneras.
**Se pueden incluir entre comillas simples ( '...') o comillas dobles ( "...") con el mismo resultados.
**\se puede usar para escapar de las comillas:
'''
print('spam eggs')
print('Doesn\'t')# use \' to escape the single quote
print("Doesn't")
print('"Yes," they said')
print('"Isn\'t," they said.')
s = 'First Line.\nSecond Line.'
print(s)
'''*
**Si no desea que los caracteres precedidos por \sean interpretados como caracteres especiales, 
**puede usar cadenas sin procesar agregando un |r|antes de la primera cita
'''
print('C:\some\name')  # ¡aquí \ n significa nueva línea!
print(r'C:\some\name')  # tenga en cuenta la r antes de la cita
print(3 * 'un' + 'ium') #Las cadenas se pueden concatenar (pegar) con el +operador y repetir con * 'unununium'

print('Py''thon') #las cadenas se pegan

prefix = 'Py'
print(prefix + 'thon')
word = 'Python'
print(word[0] + '\n' + #Caracter en posición 0
      word[1] + '\n' + #Caracter en posición 1
      word[-1] + '\n'+ #Ultimo caracter
      word[-2] + '\n'+
      word[-6] + '\n'+
      word[0:2] + '\n'+ # caracteres de la posición 0 (incluidos) a 2 (excluidos)
      word[2:5] + '\n'+# caracteres de la posición 2 (incluidos) a 5 (excluidos)
      word[:2] + word[2:] + '\n'+ # :2 de inicio hasta llegar al 2 , 2: despues del 2 hasta el final y se unen las cadenas
      word[-2:] +'\n'+# caracteres desde el penúltimo (incluido) hasta el final
      'J' + word[:1] +'\n'+#Jython
      word[:2] + 'py'
      )
#La función incorporada len()devuelve la longitud de una cadena
s = 'supercalifragilisticexpialidocious'
s1 = 'SUPERCALIFRAGILISTICO'
print(len(s))

'''*Métodos de cadenas de texto
Las cadenas implementan todas las operaciones de secuencia comunes , junto con los métodos adicionales que se describen a continuación.
str.endswith( sufijo [ , inicio [ , fin ] ] ) ->Devuelva Truesi la cadena termina con el sufijo especificado ; de lo contrario, devuelva False. sufijo también puede ser una tupla de sufijos para buscar.
str.isalnum( ) 
Devuelve Truesi todos los caracteres de la cadena son alfanuméricos y hay al menos un carácter, de lo Falsecontrario. 
Un carácter ces alfanumérico si uno de los siguientes rendimientos True: c.isalpha(), c.isdecimal(), c.isdigit(), o c.isnumeric().
str.islower( ) 
Regrese Truesi todos los caracteres en mayúscula en la cadena están en minúsculas y hay al menos un carácter en mayúscula, de lo Falsecontrario
str.isspace( ) 
Regrese Truesi solo hay caracteres de espacio en blanco en la cadena y hay al menos un carácter, de lo Falsecontrario.
str.isupper( ) ¶
Regrese Truesi todos los caracteres en mayúscula 4 en la cadena son mayúsculas y hay al menos un carácter en mayúscula, de lo Falsecontrario.
str.join( iterable ) 
Devuelve una cadena que es la concatenación de las cadenas en iterable . Se TypeErrorgenerará A si hay valores que no sean de cadena en iterables , incluidos los bytesobjetos.

'''
print(str.capitalize(s1)) #Te devuelve la primera letra capital y el resto en minusculas, Supercalifragilistico
print(str.casefold(s)) #Devuelve una copia de la cadena con mayúsculas y minúsculas. Las cadenas plegadas en mayúsculas y minúsculas se pueden usar para emparejar sin mayúsculas
string = "Python is awesome"

new_string = string.center(24, '*')

print("Centered String: ", new_string) #Centered String:  ***Python is awesome**** string.center(width[, fillchar])
# new_string = string.center(50, '*') ****************Python is awesome*****************

