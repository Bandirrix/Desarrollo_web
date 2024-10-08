var inicio = new Date().getTime(); // Alcance global que arroja el tiempo en milisegundos 
function obtenerColorAleatorio() // Esta funcion genera un color random basandose en el sistema hexadecimal 
{
    var letra = "0123456789ABCDEF".split("");
    var color = "#";
    for (var i = 0; i < 6; i++) {
        color += letra[Math.round(Math.random() * 15)];
    }
    return color;
}

function aparecerforma() {
    var top = Math.random() * 400 + "px"; //posicion aleatoria entre 0 y 400 px
    var left = Math.random() * 400 + "px";
    var width = (Math.random() * 200) + 100 + "px"; // Esta variable o que hace es que le da una anchura random entre 0 y 200 pero con el extra de darle 100px extras para que minimo sea 100px
    var colorAleatorio = obtenerColorAleatorio();

    if (Math.random() > 0.5) {
        document.getElementById("forma").style.borderRadius = "50%";
    }
    else {
        document.getElementById("forma").style.borderRadius = "0%";
    }
    document.getElementById("forma").style.display = "block"; // se declara una función donde se genera el cuadro de nuevo
    document.getElementById("forma").style.width = width;
    document.getElementById("forma").style.height = width;
    document.getElementById("forma").style.top = top;
    document.getElementById("forma").style.left = left;
    document.getElementById("forma").style.backgroundColor = colorAleatorio;

    inicio = new Date().getTime();
}

function aparecerFormaDespuesDeRetraso() {
    setTimeout(aparecerforma, Math.random() * 2000);
}
aparecerFormaDespuesDeRetraso();
document.getElementById("forma").onclick = function () {
    document.getElementById("forma").style.display = "none";
    var fin = new Date().getTime();
    var diferencia = (fin - inicio) / 1000; // Aqui se divide entre 1000 para convertir en segundos 
    document.getElementById("tiempoReaccion").innerHTML = diferencia + "s";
    // setTimeout(aparecerforma,2000); // Establece un timer en el cual se usará la funcion "aparecerforma" en 2000 milisegundos
    aparecerFormaDespuesDeRetraso();
}