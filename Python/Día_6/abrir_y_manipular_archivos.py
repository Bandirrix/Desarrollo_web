# E/S (Entradas/ salidas) o I/O 8inputs/outputs
# https://www.reddit.com/r/learnpython/comments/10mowgc/trouble_with_vs_code_calling_a_text_file_to_read/
# Dando clik derecho en el archivo que deseas abrir te aparece la ruta relativa, la cual, aparentemente tienes que poner porque de lo contreario no va a saber que archivo buscas
# Al ser strings, puedes usar todos los metodos de los strings 

mi_archivo = open('Python\Día_6\prueba.txt') #Primero se necesita abrir el archivo 
print(mi_archivo.read()) # En esta línea se lee el archivo y se imprime al mismo tiempo
 #Para gestionar mejor la memoria, se recomienda cerrar los archivos luego de usarlos 
print('***********')

mi_archivo = open('Python\Día_6\prueba.txt')
una_linea = mi_archivo.readline() #Lee el archivo pero solo linea por linea 
print(una_linea)
                                  # Este metodo lo que hace es que luego de leer una linea, se queda en el punto despues de la primer lectura, por lo que al ejecutar de nuevo el readline muestra la lines siguiente
una_linea = mi_archivo.readline()
print(una_linea.rstrip()) #El edito de texto tiene marcado el salto de linea que no vemos pero que python sí interpreta, por eso sale todo separado. La usar este metodo elimina ese salto de linea

una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo = open('Python\Día_6\prueba.txt') #EL archivo es una coleccion de lineas, por lo que puedes iterar dentro de ellas y cambiarlas o hacer diversas cosas en cada iteracion
for l in mi_archivo:
    print("Aqui dice: " + l)

mi_archivo = open('Python\Día_6\prueba.txt')
todas = mi_archivo.readlines() #Genera una lista llena de cada linea que contiene el archivo. Terner en cuenta que cada vez que ejecutas este metodo se carga el archivo la veces que sea llamado el metodo, por lo que una mala gestion de estas podria hacer que te quedes sin memoria 
print(todas)

 

mi_archivo.close()