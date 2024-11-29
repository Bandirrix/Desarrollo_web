SELECT * FROM users ORDER BY age;
/* Con el ORDER BY puedes darle un campo en el cual quieres que se base la consulta para ordernarlo, como en este caso es por la edad. 
Por defecto los datos se van a organzar de manera ascendente */

SELECT * FROM users ORDER BY age ASC;
/*Se puede especificar que sea de orden ascendente */

SELECT * FROM users ORDER BY age DESC;
/*Se puede especificar que sea de orden descendente */

SELECT * FROM users WHERE email="corona.fer07@gmail.com"  ORDER BY age DESC;
/*En este como en varias sentencias, se puede hacer mas especificas y complejas, agregando diferentes variables dentro de la misma */