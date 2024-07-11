const searchContainer = document.querySelector('.search-input-box');
const inputSearch = document.getElementById('producto');
const inputID = document.getElementById('id');
const inputPrecio = document.getElementById('precio');
const boxSuggestions = document.querySelector(
	'.container-suggestions'
);
const cuerpoTabla = document.getElementById('cuerpoTabla');

let venPro = [];
let listFac = [];

const searchLink = document.querySelector('a');

inputSearch.onkeyup = e => {
	let userData = e.target.value;
	let emptyArray = [];
	const secondElement = ""
	let id = ""
	let precio = ""

	if (userData) {
		emptyArray = suggestions.filter(data => {
			const secondElement = data[1];
			return secondElement
				.toLocaleLowerCase()
				.startsWith(userData.toLocaleLowerCase());
		});
		id = emptyArray[0][0];
		precio = emptyArray[0][4];
		emptyArray = emptyArray.map(data => {
			return (data = `<li>${data[1]}</li>`);
		});
		searchContainer.classList.add('active');
		showSuggestions(emptyArray);

		let allList = boxSuggestions.querySelectorAll('li');

		allList.forEach(li => {
			li.setAttribute('onclick', `select(${precio},${id}, this)`);
		});
	} else {
		searchContainer.classList.remove('active');
	}
};

function select(precio, data, element) {
	let selectUserData = element.textContent;
	inputSearch.value = selectUserData;
	inputID.value = data 
	inputPrecio.value = precio
	searchContainer.classList.remove('active');
}

const showSuggestions = list => {
	let listData;

	if (!list.length) {
		userValue = inputSearch.value;
		listData = `<li>${userValue}</li>`;
	} else {
		listData = list.join(' ');
	}
	boxSuggestions.innerHTML = listData;
};

function agregarElementos() {
	const elemento1 = document.getElementById('id').value;
	const elemento2 = document.getElementById('producto').value;
	const elemento3 = parseFloat(document.getElementById('precio').value); // Convertir precio a número
	const elemento4 = parseFloat(document.getElementById('cantidad').value);
  
	if ((elemento1 || elemento2 || elemento3) && elemento4) {
		const nuevaFila = document.createElement('tr');
		const nuevaCelda1 = document.createElement('td');
		const nuevaCelda2 = document.createElement('td');
		const nuevaCelda3 = document.createElement('td');
		const nuevaCelda4 = document.createElement('td');
		const nuevaCeldaAcciones = document.createElement('td');
		const botonEliminar = document.createElement('button');
		const subtotal = elemento3 * elemento4;

		
		venPro.push(elemento1);
		venPro.push(elemento4);
		venPro.push(subtotal);

		listFac.push(venPro);

		venPro = [];

		botonEliminar.textContent = 'Eliminar';
		// Agrega un evento click al botón para eliminar la fila
		botonEliminar.addEventListener('click', () => {
			nuevaFila.parentNode.removeChild(nuevaFila); // Elimina la fila padre del botón
			const totalAnterior = parseFloat(document.getElementById('total').textContent) || 0;
			const nuevoTotal = totalAnterior - subtotal;
			document.getElementById('total').textContent = nuevoTotal.toFixed(2);
		  });
	
		nuevaCelda1.textContent = elemento1;
		nuevaCelda1.id = "idproducto";
		nuevaCelda2.textContent = elemento2;
		nuevaCelda3.textContent = elemento4;
		nuevaCelda4.textContent = subtotal.toFixed(2);

		// Agregar el formulario a la celda de acciones
		nuevaCeldaAcciones.appendChild(botonEliminar);

		nuevaFila.appendChild(nuevaCelda1);
		nuevaFila.appendChild(nuevaCelda2);
		nuevaFila.appendChild(nuevaCelda3);
		nuevaFila.appendChild(nuevaCelda4);
		nuevaFila.appendChild(nuevaCeldaAcciones); 
  
		// Agregar la fila a la tabla
		cuerpoTabla.appendChild(nuevaFila);

		// Sumar el subtotal y actualizar el total
		const totalAnterior = parseFloat(document.getElementById('total').textContent) || 0;
		const nuevoTotal = totalAnterior + subtotal;
		document.getElementById('total').textContent = nuevoTotal.toFixed(2);

  
		// Limpiar los inputs
		document.getElementById('id').value = '';
		document.getElementById('producto').value = '';
		document.getElementById('precio').value = '';
		document.getElementById('cantidad').value = '';
	}
  }

function obtenerValores() {
	const total = document.getElementById("total").value;
	const nombre = document.getElementById("nombre").value;
	const correoElectronico = document.getElementById("correoElectronico").value;
}

function facturar(){
	listT = []
	listC = []

	const total = parseFloat(document.getElementById('total').textContent);
	const nombre = document.getElementById('nombre').value;
	const email = document.getElementById('email').value;
	const telefono = document.getElementById('telefono').value;

	listC.push(nombre)
	listC.push(email)
	listC.push(telefono)

	console.log(listC)

	listT.push(total)
	listT.push(total)
	listT.push(total)

	listFac.push(listC)
	listFac.push(listT)

	document.getElementById('myModal').style.display = 'none';

	const xhr = new XMLHttpRequest();
	xhr.open('POST', '/vender/factura');
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
	xhr.send(JSON.stringify(listFac));

	listFac = []
	listT = []
}

function abrirModal() {
	
	document.getElementById('total_modal').textContent = document.getElementById('total').textContent;
	document.getElementById('myModal').style.display = 'block';

}

// Función para cerrar el modal
function cerrarModal() {
	document.getElementById('myModal').style.display = 'none';
}

