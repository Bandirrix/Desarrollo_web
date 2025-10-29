# E/S o I/O
# https://www.reddit.com/r/learnpython/comments/10mowgc/trouble_with_vs_code_calling_a_text_file_to_read/
# Dando clik derecho en el archivo que deseas abrir te aparece la ruta relativa, la cual, aparentemente tienes que poner porque de lo contreario no va a saber que archivo buscas

mi_archivo = open('Python\Día_6\prueba.txt')
print(mi_archivo.read())
mi_archivo.close()
print('***********')

mi_archivo = open('Python\Día_6\prueba.txt')
una_linea = mi_archivo.readline()
print(una_linea)
