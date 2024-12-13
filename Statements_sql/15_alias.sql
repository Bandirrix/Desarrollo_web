/*ALIAS*/

/*Con este comando, puedes asignarle un nombre a cierta columna que estas consultando
para asi poder catigorizar de una manera mas personalizada*/

SELECT name, init_date AS "Fecha de inicio en programacion" FROM users WHERE name = 'Fernando';
/*Aqui se hace la consulta de dato de un rango donde pedimos que nos muestre el nombre y la fecha de inicio
 y con el comando AS luego del dato que queremos, colocamos la palabra reservada AS para darle el nombre que
 queramos a la consulta*/

/*CONCAT*/

/*Con el comando CONCAT, puedes como dice este, concatenar cualquier columna dentro de una sola, agregando texto dentro de esta para poder mostrarlo de una 
manera diferente*/

SELECT CONCAT('Nombre: ', name, ', Apellido: ', last_name) FROM users;
/*Concatena los datos de la columna name y last_name y agrega cadenas para identificar cada apartado*/

SELECT CONCAT('Nombre: ', name, ', Apellido: ', last_name)  AS 'Nombre completo' FROM users;
/*Concatena los datos de la columna name y last_name y agrega cadenas para identificar cada apartado, a demas de darle un nombre a la columna de consulta*/