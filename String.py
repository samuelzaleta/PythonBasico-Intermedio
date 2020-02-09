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
print(len(s))
