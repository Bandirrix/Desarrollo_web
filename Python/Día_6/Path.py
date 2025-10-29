# Path nos sirve para representar una ruta de un archivo o carpeta en nuestra computadora pero sin crearlas? 
# Crear y mover archivos / enumear archivos / crear rutas basadas en strings (crear una gerarquia de carpetas)

from pathlib import Path

base = Path.home() # Muestra la ruta base de tu computadora
print(base)
guia = Path('Europa', 'España', 'Barcelona', 'Sagrada_Familia.txt') #Generar / Obtener una ruta relativa sin necesidad de poner la ruta base
print(guia)
guia1 = Path(base, 'Europa', 'España', Path('Barcelona', 'Sagrada_Familia.txt')) #Dentro del objeto Path, se pueden usar cadenas u otras variables tipo Path, ya que esta las reconoce, así como "concatenar objetos Path dentro de mismo, dando el mismo resultado"
print(guia1) 
guia2 = guia1.with_name('La_Pedrera.txt') #with_name usa la ruta que contenga el objeto Path, excluyendo el archivo que especifica este mismo
print(guia2)
print(guia1.parent) #Devuelve la carpeta anterior mas proxima de la ruta
print(guia1.parent.parent) #Se puede usar varias veces para ir recorriendo los ancentros de las carpetas (carpertas ateriores)

guia3 = Path(Path.home(), 'Europa')
for txt in Path(guia3).glob('*.txt'): #glob engloba lo que haya dentro de una carpeta especificada y esto, ligado al bucle for, puedes enlistar lo que hay dentro de dicha carpeta pero sin entrar a las subcarpetas
    print(txt)
for txt in Path(guia3).glob('**/*.txt'): #**/* incluye todas las carpetas y subcarpetas dentro de la carpeta elegida 
    print(txt)