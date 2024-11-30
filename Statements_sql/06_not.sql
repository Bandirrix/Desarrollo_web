/*NOT, AND Y OR */

/*Consulta condicionante tipo NOT, AND Y OR
Estas consultas trabajan de la misma manera con un WHERE, donde la palabra reservada indica como se hará la consulta*/
SELECT * FROM users WHERE NOT email = "luis@gmail.com";
/*Con esta consulta, mostrará todos los dato que son diferentes a la cadena o valor escrito */
SELECT * FROM users WHERE NOT email = "luis@gmail.com" AND age = 44;
/*Aqui con el AND lo que hace es agragar una condicion a la consula, en la cual se muestra lo diferente al valor indicado y, ademas, los datos
que sí coincidan con la siguiente consulta*/
SELECT * FROM users WHERE NOT email = "corona.fer07@gmail.com" OR age = 12;
/*Aqui con el OR lo que hace es agragar una condicion a la consula, en la cual se muestra lo diferente al valor indicado o los datos
que sí coincidan con la siguiente consulta*/