/*LIMIT*/

/*Como su nombre lo indica, este modificador de consulta limita le numero de valores que se mostraran en los resultados, ayudando a restringir los 
valores en bases de datos de una cantidad inmensa de datos*/
SELECT * FROM users LIMIT 2;
/*Limita los datos al numero especificado*/

SELECT * FROM users WHERE NOT email = "corona.fer07@gmail.com" OR age = 12 LIMIT 2;
/*A una consulta normal, se pude restringir el numero de los datos arrojados, estos de manera ascendente por el id*/