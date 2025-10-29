#Dentro del metodo open, se tiene 3 metodos para hacerlo, con "r" de lectura, "w" de escritura y la "a" de solo escritura al final del texto 

'''archivo = open('Python\Día_6\prueba.txt', 'r')
archivo.write('soy la nueva linea')               #Al querer escribrir con el metodo write en solo lectura nos arroja un error
archivo.close()'''

archivo = open('Python\Día_6\prueba1.txt', 'w') #Con esta linea si no existe el archivo, lo crea. y si ya exite el archivo, lo sobreescribe 
archivo.write('Soy una nueva linea de texto \n') # Si no pones alto de linea, el texto se concatena luego luego del otro
archivo.write('''YO 
              iguanas  
              ranas''') #Así escribes con saltos de linea directamente 
archivo.writelines(['hola', 'mundo','como','estan?']) #Agrega lineas de texto en base a una lista, pero estas las pone seguidas sin espacio 

archivo1 = open('Python\Día_6\prueba.txt', 'a') #Con el modo a escribe luego de lo que escribiste en el archivo, no lo sobreescribe
archivo1.write('bienvenido')

'''
lista = ['hola', 'mundo','como','estan?']
for p in lista:                             "Con esto puedes hacer uso del writelines pero poniendo los separadores o los saltos de linea
archivo.writelines(p + '\n')
'''