from pathlib import Path, PureWindowsPath
# Control + F para remplazar todo de una sola linea
# No es necesario cerrar y abrir usando el metodo Path
#Todos los metodos termian con "()", por lo que no los tienen son considerados otras cosas

carpeta = Path('C:/Users/coron/Documents/Desarrollo_web/Desarrollo_web/Python/Día_6/prueba.txt')
print(carpeta.read_text()) #Leer un archivo
print(carpeta.name) #Obtener el nombre del archivo 
print(carpeta.suffix) #Obtener el tipo del archivo
print(carpeta.stem) #Obtener el nombre del archivo sin la terminacion de este

if not carpeta.exists(): #Verificar si esxiste un archivo se usa el metodo exists()
    print('Este archivo no existe')
else:
    print("Sí existe, yeah!")

ruta_windows = PureWindowsPath(carpeta) #Con esta nueva importacion de PureWindowsPath podemos obtener las rutas del modo que son mostradas en el sistema operativo de windows
print(ruta_windows)
 


