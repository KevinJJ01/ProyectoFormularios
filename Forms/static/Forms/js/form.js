// Lista desplegable
// Elementos del DOM
const selectElement = document.getElementById("dynamicSelect");
const inputElement = document.getElementById("newOption");
const addButton = document.getElementById("addOption");

// Evento para agregar nuevas opciones al select
addButton.addEventListener("click", () => {
  const newOptionValue = inputElement.value.trim(); // Obtiene el texto del input y elimina espacios extra

  if (newOptionValue) {
    // Crear una nueva opción
    const newOption = document.createElement("option");
    newOption.value = newOptionValue.toLowerCase(); // Asigna un valor único en minúsculas
    newOption.textContent = newOptionValue; // Texto visible para el usuario

    // Agregar la nueva opción al select
    selectElement.appendChild(newOption);

    // Limpiar el input
    inputElement.value = "";
  } else {
    alert("Por favor, escribe una opción válida.");
  }
});

// Función para agregar las opciones al formulario oculto para enviarlas en el POST
document.querySelector('form').addEventListener('submit', function (event) {
  const select = document.getElementById("dynamicSelect");
  const opciones = "";

  // Recolectar todas las opciones del select
  for (let i = 0; i < select.options.length; i++) {
    opciones.push(select.options[i].value); // Obtener el valor de cada opción
  }

  // Añadir cada opción como un campo oculto independiente
  opciones.forEach(opcion => {
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'opciones'; // Mantén el mismo nombre que en el backend
    input.value = opciones;
    this.appendChild(input);
  });
});

// Función para agregar una nueva opción al contenedor de opciones (si se usa para checkbox, por ejemplo)
function agregarOpcion(formType) {
  let containerId =
    formType === 1 ? "options-container-1" : "options-container-2";
  let container = document.getElementById(containerId);

  // Crear un nuevo elemento de opción (input)
  let newOptionDiv = document.createElement("div");
  if (formType === 1) {
    newOptionDiv.innerHTML =
      '<div><input class="checkbox" type="checkbox"><input class="option" type="text" id="opciones" name="opciones" placeholder="Titulo opcion" required></div></div>';
  } else {
    console.log("Error al crear nuevo input");
  }
  // Agregar el nuevo elemento al contenedor
  container.appendChild(newOptionDiv);
}