-- NULL

/*Con este comando, lo que hace referencia la consula es que buscas los campos que estan vacios */

SELECT * FROM users WHERE email IS NULL;
/*Muestra los datos que contienen ciertos campos vacios, en este caso el email*/

SELECT * FROM users WHERE email IS NOT NULL;
/*Muestra los datos que no contienen ciertos campos vacios, en este caso el email*/

SELECT * FROM users WHERE email IS NOT NULL AND age = 25;
/*Se añade la instrución de que muestre los datos que ademas contenga la edad estipulada*/