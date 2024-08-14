let listFactura = [];
let listaFac = [];

//Buscador de contenido

//Declarando variables
inputSearch =       document.getElementById("inputSearch");
box_search =        document.getElementById("box-search");

//Creando filtrado de busqueda

document.getElementById("inputSearch").addEventListener("keyup", buscador_interno);

function buscador_interno(){


    filter = inputSearch.value.toUpperCase();
    li = box_search.getElementsByTagName("li");

    //Recorriendo elementos a filtrar mediante los "li"
    for (i = 0; i < li.length; i++){

        textValue = li[i].textContent;

        if(textValue.toUpperCase().indexOf(filter) > -1){

            li[i].style.display = "";
            box_search.style.display = "block";

            if (inputSearch.value === ""){
                box_search.style.display = "none";
            }

        }else{
            li[i].style.display = "none";
        }
    }
}

function guardarProducto(productoCompleto) {
    
    // Eliminar paréntesis y comillas
    const strSinComillas = productoCompleto.replace(/[\(\)]|['"]/g, "");

    // Dividir la cadena por comas
    const lista = strSinComillas.split(",");

    // Convertir los elementos a sus tipos de datos correspondientes
    const listaConvertida = lista.map((elemento, index) => {
        // Convertir a números enteros si son numéricos
        if (index === 0 || index === 3 || index === 4) {
        const numero = parseFloat(elemento.replace(/,/g, "")); // Eliminar comas
        if (!isNaN(numero)) {
            return numero;
        }
        }
    
        // Dejar el resto como cadenas
        return elemento.trim();
    });

    listaFac.push(listaConvertida);

    const precio = listaConvertida[4],
    producto = listaConvertida[1];
    document.getElementById('input-precio').value = precio;
    document.getElementById('inputSearch').value = producto;

    box_search.style.display = "none";

}

const boton = document.getElementById("miBoton");

boton.addEventListener("click", listar);

function listar(){
    
    let contador = 0;
    let subtotal = 0;
    let totalA = 0;
    let listaPro = [];

    const tabla = document.getElementById('myTableBody'),
        cantidad = document.getElementById('input-cantidad').value, 
        precio = document.getElementById('input-precio'),
        totalI = document.getElementById('total');

    if (cantidad != 0) {
        for (const datos of listaFac) {
            listaPro = [];
            const fila = document.createElement("tr");

            const celda0 = document.createElement("td");
            celda0.textContent = contador + 1;
            fila.appendChild(celda0);

            const celda1 = document.createElement("td");
            celda1.textContent = datos[1];
            fila.appendChild(celda1);
            listaPro.push(datos[0])

            const celda2 = document.createElement("td");
            celda2.textContent = cantidad;
            fila.appendChild(celda2);
            listaPro.push(cantidad);

            const celda3 = document.createElement("td");
            subtotal = datos[4] * cantidad;
            celda3.textContent = subtotal;
            fila.appendChild(celda3);
            listaPro.push(subtotal)

            totalA = parseInt(totalI.textContent) || 0;
            totalA = totalA + subtotal;

            totalI.textContent = totalA;

            tabla.appendChild(fila);
            listFactura.push(listaPro);
        }
    }
}

function facturar(){

	listT = [];
	listC = [];

	const total = parseFloat(document.getElementById('total').textContent);
	const nombre = document.getElementById('cliente').value;
	const email = document.getElementById('email').value;
	const telefono = document.getElementById('telefono').value;
    console.log("nyaaaa");

	listC.push(nombre);
	listC.push(email);
	listC.push(telefono);

	listT.push(total);
	listT.push(total);
	listT.push(total);

	listFactura.push(listC);
	listFactura.push(listT);

	const xhr = new XMLHttpRequest();
	xhr.open('POST', '/vender');
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.onload = function() {
		if (xhr.status === 200) {
			if (xhr.responseURL.includes('/vender')) {
			  console.log('Lista enviada y redirección a /vender exitosa');

				while (cuerpoTabla.firstChild) {
					cuerpoTabla.removeChild(cuerpoTabla.firstChild);
					document.getElementById('total').textContent = "";
				  }
				
			} else {
			  console.error('Error al enviar la lista:', xhr.statusText);
			}
		  } else {
			console.error('Error al enviar la lista:', xhr.statusText);
		  }
	};
	xhr.send(JSON.stringify(listFactura));

	listFactura = [];
}
