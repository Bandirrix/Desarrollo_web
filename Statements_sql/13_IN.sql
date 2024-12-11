/*IN*/

/*Este comando se usa para poder hacer consultas cuando se sabe excatamente que 
es lo que quieres consultar, ya que si no especificas bien lo que quieres consultar, no sale el dato necesario*/
/*Cuando especificas la cadeena que quieres consultar, se debe de hacer con comilla sencilla*/
SELECT * FROM users WHERE name IN ('LUIS');
/*Se consulta datos que contengan el nombre de LUIS*/

SELECT * FROM users WHERE name IN ('LUIS', 'CARLOS');
/*Se consulta datos que contengan el nombre de LUIS o de CARLOS*/