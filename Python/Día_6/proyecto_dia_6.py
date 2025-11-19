# Hacer un administrador de recetas 
# En la carpeta base se crea una carpeta que se llame recetas en la cual habrá 4 carpertas (carnes, ensaladas, pastas, postres)
# Y Cada una de las carpetas tendrá 2 archivos .txt con información o no relevante 
# 1. Saludo de bienvenida
# 2. En qeu directiro está la carpeta 
# 3. La cantidad de recetas que se tiene
from pathlib import Path
import os 

print('Bienvenida/o a tu recetario de pura calidad ')
base = Path.home()
ruta_base = Path(base, 'Recetas')
print(f"Tu recetario está guardado en: {ruta_base}")
num_recetas = 0
for txt in Path(ruta_base).glob('**/*.txt'):
    num_recetas += 1
print(f"Tienes {num_recetas} recetas")
opciones = ['1. Leer receta', '2. Crear receta', '3. Crear categoria', '4. Eliminar receta', '5. Eliminar categoria', '6. Finalizar programa']
ruta_interna = ''
def escoger_categoria (opciones):
    for i in opciones:
        print(i)
    eleccion = input(print("¿Qué opción escoges?: "))
    return eleccion

def elegir_categoria ():
    print('Aquí se muestran las categorias actuales: ')
    for carpeta in Path(ruta_base).glob('*'):
        print(os.path.basename(carpeta))
    elec_categoria = input('Digita el numero de la categoria que deseas elegir:')
    
    return elec_categoria

def mostrar_recetas (entrada_x):
    ruta_interna = Path(entrada_x)
    for txt in Path(ruta_interna).glob('*/.txt'):
        print(txt)
    return

#def elegir_receta():
     

#Elegir receta
#Leer receta
#Crear receta
#Crear contenido 
#Crear categoria 
#Eliminar recetas
#Eliminar categoria
#Finalizar codigo 
        
        


'''
while True:
    print("Escoge una de las suguientes opciones: ")
'''


