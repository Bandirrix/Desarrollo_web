SELECT * FROM users WHERE age = 25;
/* con el where lo que se puede hacer es que te permite poder especificar un apartado que te ayuda a hacer las consultas de una mejor manera
en el caso de la sentencia que ser muestra, lo que busca es dentro de users muestre los usuarios que tengan una edad igual a 25. */
SELECT name FROM users WHERE age = 25;
/* Mostrar los nombre del usuario que coinciden con la edad = 25 */ /* */
SELECT DISTINCT age FROM users WHERE age = 25;
/*Mostrar y grupar la edad que coincida con el valor del where*/
SELECT DISTINCT name FROM users WHERE age = 25;
/*Mostrar y grupar el nombre que coincida con el valor del where*/