-- COUNT

--Con este comando cuenta el numero de valores que no son nulos de un campo especifico (renglones)

SELECT COUNT(*) FROM users;
 -- EN este caso, cuenta el numero de datos (renglones que hay en la tabla)

SELECT COUNT(email) FROM users;
 -- EN este caso, cuenta el numero de datos que hay en el campo email (renglones que hay en la fila)