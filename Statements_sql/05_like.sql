/*LIKE*/
 
/*Sintaxis: Para poder usar el LIKE es necesario el uso del WHERE, ya que se entiende como donde cierto campo sea como  tal. El uso del % es un 
wildcard, que dice que ante o despues de cierta cadena puede ser cualquier cosa */

SELECT * FROM users WHERE email LIKE "%gmail.com";
/*En este caso se muestran los datos que tienen un gmail.com y lo anterior es lo que sea*/

SELECT * FROM users WHERE email LIKE "luis%";
/*En este caso se muestran los datos que tienen un luis y lo demas puede ser lo que sea */

SELECT * FROM users WHERE email LIKE "%@%";
/*Aqui lo unico que importa es el @, antes y despues de este simbolo es indiferente */