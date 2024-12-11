/*ALIAS*/

/*Con este comando, puedes asignarle un nombre a cierta columna que estas consultando
para asi poder catigorizar de una manera mas personalizada*/

SELECT name, init_date AS "Fecha de inicio en programacion" FROM users WHERE name = 'Fernando';
/*Aqui se hace la consulta de dato de un rango donde pedimos que nos muestre el nombre y la fecha de inicio
 y con el comando AS luego del dato que queremos, colocamos la palabra reservada AS para darle el nombre que
 queramos a la consulta*/