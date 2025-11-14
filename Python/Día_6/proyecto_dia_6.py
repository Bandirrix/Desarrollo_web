# Hacer un administrador de recetas 
# En la carpeta base se crea una carpeta que se llame recetas en la cual habrá 4 carpertas (carnes, ensaladas, pastas, postres)
# Y Cada una de las carpetas tendrá 2 archivos .txt con información o no relevante 
# 1. Saludo de bienvenida
# 2. En qeu directiro está la carpeta 
# 3. La cantidad de recetas que se tiene
from pathlib import Path

print('Bienvenida/o a tu recetario de pura calidad ')
base = Path.home()
ruta_base = Path(base, 'Recetas')
print(f"Tu recetario está guardado en: {ruta_base}")
num_recetas = 0
for txt in Path(ruta_base).glob('**/*.txt'):
    num_recetas += 1
print(f"Tienes {num_recetas} recetas")


