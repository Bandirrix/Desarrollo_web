/*GROUP BY*/

/*EL GROUP BY genera una columna resumen, agrupa los datos de una consulta en relacion a una columna que nosotros queramos asignarle, solo
que no puede trabajar así solo, necesita tener otro comando que ayude a saber como lo va a agrupar */

SELECT MAX(age) FROM users GROUP BY age;
/*Selecciona el maximo de la edad de una tabla y lo agrupa por edades, sin repetir los datos que se están consultnado*/
SELECT COUNT(age), age FROM users GROUP BY age;

SELECT COUNT(age), age FROM users GROUP BY age ORDER BY age ASC;

SELECT COUNT(age), age FROM users WHERE age > 15 GROUP BY age ORDER BY age ASC;