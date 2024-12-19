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
  console.log("Formulario enviado, procesando opciones...");
  const select = document.getElementById("dynamicSelect");
  const opciones = [];

  // Recolectar todas las opciones del select (sin incluir la opción "Selecciona una opción")
  for (let i = 0; i < select.options.length; i++) {
    const option = select.options[i];
    if (option.value && option.value !== "Selecciona una opcion") {
      opciones.push(option.value); // Obtener el valor de cada opción
    }
  }

  console.log("Opciones recolectadas:", opciones);  // Verifica qué opciones estamos obteniendo del form

  if (opciones.length === 0) {
    alert("Por favor, agrega al menos una opción.");
    event.preventDefault();  // Detener el envío si no hay opciones
    return;
  }

  // Añadir cada opción como un campo oculto
  opciones.forEach(opcion => {
    const input = document.createElement("input");
    input.type = "hidden";
    input.name = "opciones";  // Nombre de los campos ocultos
    input.value = opcion;
    this.appendChild(input);  // Añadir el campo oculto al formulario
  });

  console.log("Campos ocultos añadidos:", opciones);  //revisar en consola si las opciones si se agregaron 

});



// Función para agregar una nueva opción al contenedor de opciones (para inputs de tipo checkbox)
function agregarOpcion(formType) {
  let containerId =
    formType === 1 ? "options-container-1" : "options-container-2";
  let container = document.getElementById(containerId);

  // Crear un nuevo elemento de opción (input)
  let newOptionDiv = document.createElement("div");
  if (formType === 1) {
    newOptionDiv.innerHTML =
      '<div><input class="checkbox" type="checkbox" name="opciones"><input class="option" type="text" placeholder="Titulo opción" required></div>';
  } else {
    console.log("Error al crear nuevo input");
  }
  // Agregar el nuevo elemento al contenedor
  container.appendChild(newOptionDiv);
}
