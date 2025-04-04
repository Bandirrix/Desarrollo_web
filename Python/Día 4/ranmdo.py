# Numeros aleatorios (Uso de metodos de una libreria externa) randit 

# from random import randint -- Con control + barra espaciadora pueden salir sugerencias de los posibles métodos que podrías utilizar 
                           # Es importante que no uses el mismo nombre de la libreria que vas a usar, porque importarias el mismo modulo que estás escribiendo
from random import * #Con el asterisco importas toda la librería, no solo un método 

aleatorio = randint(1,50) #Especificar un el rango en el cual se estará trabajando 
print(aleatorio)

aleatorio1 = round(uniform(1,5),1) #Generar un numero aleatorio tipo float. Con el round especificas el numero de decimales que quieres
print(aleatorio1)

aleatorio2 = random() # Numero aleatorio entre 0 y 1 
print(aleatorio2)

colores = ['azules','verdes','rojos','amarillos']
aleatorio3 = choice(colores) #Escoge un item aleatorio de un coleccionable
print(aleatorio3)

numeros = list(range(5,50,5))
shuffle(numeros) #Hace una mezcla de los numero en el sitio, por lo que no es posible almacenarla tal cual, y con los string no trabaja ya que son inmutables
print(numeros)

