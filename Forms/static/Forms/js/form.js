// Lista desplegable
// Elementos del DOM
const selectElement = document.getElementById("dynamicSelect");
const inputElement = document.getElementById("newOption");
const addButton = document.getElementById("addOption");

// Función para agregar una nueva opción al contenedor de opciones (si se usa para checkbox, por ejemplo)
function agregarOpcion(formType) {
  let containerId =
    formType === 1 ? "options-container-1" : "options-container-2";
  let container = document.getElementById(containerId);

  // Crear un nuevo elemento de opción (input)
  let newOptionDiv = document.createElement("div");
  if (formType === 1){
    newOptionDiv.innerHTML =
    '<div><input class="checkbox" type="checkbox"><input class="option" type="text" id="opciones" name="opciones" placeholder="Titulo opcion" ></div>'
    container.appendChild(newOptionDiv);
  } 
  else if (formType === 2) {
    // Cambiar los inputs existentes a tipo "hidden"
    let inputs = container.querySelectorAll('input[type="text"]');
    if (inputs.length > 0) {
      inputs.forEach((input) => {
        input.type = "hidden";
      });
    }

    newOptionDiv.innerHTML =
      '<div><input class="option" type="text" name="opciones" id="opciones" placeholder="Escribe nueva opción" required></div>';
    container.appendChild(newOptionDiv);

    // Obtener el valor del nuevo input
    let newInput = newOptionDiv.querySelector('input[type="text"]');
    newInput.addEventListener("change", function () {
      agregarAlSelect(this.value);
    });
  } else {
    console.log("Error al crear nuevo input");
    return;
  }
}

// Función para agregar una opción al <select>
function agregarAlSelect(valor) {
  if (valor.trim() === "") {
    console.warn("El valor ingresado está vacío.");
    return;
  }

  let select = document.getElementById("dynamicSelect");
  if (!select) {
    console.error("El elemento <select> no existe.");
    return;
  }

  // Crear una nueva opción y agregarla al <select>
  let newOption = document.createElement("option");
  newOption.value = valor;
  newOption.textContent = valor;
  select.appendChild(newOption);
}




