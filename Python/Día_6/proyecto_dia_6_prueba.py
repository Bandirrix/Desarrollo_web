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

def escoger_opcion (opciones):
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
    # Meter si quiero el numero de la categoria o el nombre de la categoria y devolver eso para la siguiente, ya que necesito la ruta de al cual quiero hacer uso 
    # Meter if para obtner la ruta y pasarla 
    return ruta_relat

def mostrar_recetas (entrada_x):
    ruta_interna = Path(entrada_x)
    lista_recetas = [] #Lista para guardar los nombres de los archivos y poder sacar la ruta
    for txt in Path(ruta_interna).glob('*.txt'):
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

    return ruta_archivo

def escribir_en_receta(ruta_archivo):
    ruta = Path(ruta_archivo)
    archivo = open(ruta, 'w')
    anw = ''
    archivo.write(input('\nAñade una linea de texto: '))
    archivo.close()
    return

def nombre_categoria():
    nombre_carpeta = input("Escribe el nombre de la categoria que deseas. En lugar de espacios, usa '_': ")

    return nombre_carpeta

def crear_categoria(nombre_carpeta):
    carpeta = Path(ruta_base,nombre_carpeta)
    os.makedirs(Path(carpeta))
    print('Listo, te muestro las categoria que tienes actualmente...')
    for cpt in Path(ruta_base).glob('*'):
        print(cpt)
    return

def eliminar_receta(ruta_relat):
    ruta_actual_defi = Path(ruta_relat)
    if ruta_actual_defi.exists():
        ruta_actual_defi.unlink()
        print(f'El archivo en la ruta {ruta_actual_defi} se ha borrado con exito ')
    else:
        print(f'El archivo en la ruta {ruta_actual_defi} no existe ') 
    
    return

def eliminar_categoria(ruta_relat): 
    ruta_actual_defi = Path(ruta_relat)
    if ruta_actual_defi.exists():
        os.rmdir(Path(ruta_actual_defi))
        print(f'La categoria en la ruta {ruta_actual_defi} se ha borrado con exito ')
    else:
        print(f'La categoria en la ruta {ruta_actual_defi} no existe ')

def mostrar_categorias():
    print('Aquí se muestran las categorias actuales: ')
    for carpeta in Path(ruta_base).glob('*'):
        print(os.path.basename(carpeta))
    return

while True:
    primer_eleccion = escoger_opcion(opciones)
    primer_eleccion = int(primer_eleccion)
    if primer_eleccion == 1 :
        ruta_relat_int = elegir_categoria()
        lista_recetas_int = mostrar_recetas(ruta_relat_int)
        receta_elegida_int = escoger_receta(lista_recetas_int, ruta_relat_int)
        leer_receta(receta_elegida_int)
    elif primer_eleccion == 2:
        ruta_relat_int = elegir_categoria()
        ruta_archivo_int = crear_receta(ruta_relat_int)
        escribir_en_receta(ruta_archivo_int)
    elif primer_eleccion == 3:
        nombre_carpeta_int = nombre_categoria()
        crear_categoria(nombre_carpeta_int)
        mostrar_categorias()
    elif primer_eleccion == 4:
        ruta_relat_int = elegir_categoria()
        lista_recetas_int = mostrar_recetas(ruta_relat_int)
        receta_elegida_int = escoger_receta(lista_recetas_int, ruta_relat_int)
        print(receta_elegida_int)
        eliminar_receta(receta_elegida_int)
    elif primer_eleccion == 5:
        ruta_relat_int = elegir_categoria()
        print(ruta_relat_int)
        eliminar_categoria(ruta_relat_int)
    elif primer_eleccion == 6:
        break


    









 