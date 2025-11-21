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
    eleccion = input("¿Qué opción escoges?: ")
    return eleccion

def elegir_categoria ():
    print('Aquí se muestran las categorias actuales: ')
    lista = []
    for carpeta in Path(ruta_base).glob('*'):
        lista.append(os.path.basename(carpeta)) #Aqui lo usaré para hacer la comparacion, o podria hacer la comapracion con el exist de las carpetas
        print(os.path.basename(carpeta))
    elec_categoria = input('Escribe el nombre de la categoria que deseas elegir tal cual se muestra:  ')
    elec_categoria = elec_categoria.strip()
    ruta_relat = Path(ruta_base / elec_categoria )
    print(ruta_relat)
    # Meter si quiero el numero de la categoria o el nombre de la categoria y devolver eso para la siguiente, ya que necesito la ruta de al cual quiero hacer uso 
    # Meter if para obtner la ruta y pasarla 
    return ruta_relat

def mostrar_recetas (entrada_x):
    ruta_interna = Path(entrada_x)
    lista_recetas = [] #Lista para guardar los nombres de los archivos y poder sacar la ruta
    for txt in Path(ruta_interna).glob('*/.txt'):
        print(txt)
    return lista_recetas

def escoger_receta(lista_recetas, ruta_relat):
    select = input('Escribe el nombre de la receta con su terminacion "txt", tal cual está en la pantalla: ')
    receta_elegida = Path(ruta_relat / select)

    return receta_elegida

def leer_receta(receta_elegida):
    ruta_receta = Path(receta_elegida)
    print(ruta_receta.read_text())

    return

def crear_receta(ruta_relat):
    nombre = input("Cómo deseas que se llame la receta?: ")
    nombre = nombre + '.txt'
    print(nombre)
    ruta_archivo = Path(ruta_relat / nombre)
    archivo = open(ruta_archivo, 'w')

    return

def escribir_en_receta(ruta_archivo):
    ruta = Path(ruta_archivo)
    archivo = open(ruta, 'w')
    anw = ''
    archivo.write(input('\nAñade una linea de texto: '))
    archivo.close()
    return

def nombre_categoria():
    nombre_carpeta = input("Escribe el nombre de la categoria que deseas. En lugar de espacios, usa '_': ")

    return nombre_categoria

def crear_categoria(nombre_categoria):
    carpeta = os.makedirs(Path(base / nombre_categoria))
    print('Listo, te muestro las categoria que tienes actualmente...')
    for cpt in Path(base).glob('*'):
        print(cpt)
    return

def eliminar_receta(ruta_relat):
    ruta_actual = Path(ruta_relat)
    if ruta_actual.exists():
        ruta_actual.unlink()
        print(f'El archivo en la ruta {ruta_actual} se ha borrado con exito ')
    else:
        print(f'El archivo en la ruta {ruta_actual} no existe ') 
    
    return

def eliminar_categoria(ruta_relat): 
    ruta_actual = Path(ruta_relat)
    if ruta_actual.exists():
        os.rmdir(Path(ruta_actual))
        print(f'La categoria en la ruta {ruta_actual} se ha borrado con exito ')
    else:
        print(f'La categoria en la ruta {ruta_actual} no existe ')











mostrar_recetas(ruta_base)