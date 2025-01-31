# Crear un programa que pregunte su nombre, Cuanto han vendido
# Frase con su nombre y cuanto han ganado en sus ventas, ya que ellos ganan el 13%

print("Qué tal, buenos días. Bienvenido al calculador de comisiones")
nombre = input("Cual es tu nombre?: ")
print("A continuación ingresarás la cantindad de ventas que relaizaste en el mes, \npor lo que te pedimos solo ingresar numeros")
ventas = float(input("Cual fue el monto de ventas totales del mes?: "))
comision = ventas*0.13
print(f"{nombre}, este mes generaste: \n${round(comision,3)}")