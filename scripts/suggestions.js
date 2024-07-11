const lista = document.getElementById('miLista');
const items = lista.querySelectorAll('li');
let suggestions = []; // Declarar la variable 'suggestions' como un array vacío

for (const item of items) {
  const valor = item.getAttribute('data-valor');
  const cleanStr = valor.replace(/\(|\)/g, '').replace(/'/g, '');
  const fin = cleanStr.split(', ');
  suggestions.push(fin); // Agregar cada valor a la lista 'suggestions'
}

