# Uso de path y os 
# cwd = currynt working directory // chdir = change directory // rmdir = remove directory
import os 

ruta = os.getcwd() #Obtener la ruta de donde estas trabajando 
print(ruta)
ruta = os.chdir('C:\\Users\\coron\\Desktop\\alternativo') # Cambiar la ruta de eleccion (Debes de poner doble barra invertida ya que en py es un caracter especial)
print(ruta)
archivo = open('prueba.txt')
print(archivo.read())
# ruta = os.makedirs('C:\\Users\\coron\\Desktop\\alternativo\\otra') crear una carpeta nueva 
ruta = 'C:\\Users\\coron\\Documents\\Desarrollo_web\\Desarrollo_web\\Python\\Día_6\prueba.txt'
elemento = os.path.basename(ruta) #Nombre del archivo o directorio en el que estás
print(elemento)
elemento = os.path.dirname(ruta) #nombre del directorio de donde estás ubicado el archivo
print(elemento)
elemento = os.path.split(ruta) #Obtner una tuppla donde muestra el direccotio y el nombre del archivo
print(elemento)
#os.rmdir('C:\\Users\\coron\\Desktop\\alternativo\\otra')   Borrar una carpeta

otro_archivo = open('C:\\Users\\coron\\Desktop\\alternativo\\prueba.txt') #Abrir un archivo sin cambiar el directorio se hace poniendo toda la ruta en el open

from pathlib import Path #Con el modulo pathlib y el objeto Path puedes hacer que cualquier tipo de os pueda leer el codigo sin problemas con los que abres los directorios
carpeta = Path('/Users/coron/Desktop/alternativo') #Eliminas el C: y cambias la doble barra invertida por la diagonal tradicional
archivo = carpeta / 'prueba.txt' #El "/" se usa para concatenar la ruta con el archivo que deseas abrir 
mi_archivo = open(archivo)
print(mi_archivo.read())
