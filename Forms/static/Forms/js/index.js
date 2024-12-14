document.addEventListener("DOMContentLoaded", function () {
  // Selecciona todos los iconos y menús de opciones
  var iconOptionsList = document.querySelectorAll(".icon-options");
  var optionsMenus = document.querySelectorAll(".options-menu");

  // Función para alternar la visibilidad del menú
  iconOptionsList.forEach(function (iconOptions, index) {
    iconOptions.addEventListener("click", function (event) {
      event.stopPropagation(); // Prevenir que el clic cierre el menú inmediatamente

      // Alternar el menú correspondiente al icono clickeado
      var optionsMenu = optionsMenus[index];
      optionsMenu.style.display =
        optionsMenu.style.display === "block" ? "none" : "block";
    });
  });

  // Cerrar el menú si se hace clic fuera de él
  document.addEventListener("click", function (event) {
    iconOptionsList.forEach(function (iconOptions, index) {
      var optionsMenu = optionsMenus[index];
      if (
        !iconOptions.contains(event.target) &&
        !optionsMenu.contains(event.target)
      ) {
        optionsMenu.style.display = "none";
      }
    });
  });
});

// Función para agregar una nueva opción al contenedor de opciones
function agregarOpcion(formType) {
  let containerId =
    formType === 1 ? "options-container-1" : "options-container-2";
  let container = document.getElementById(containerId);

  // Crear un nuevo elemento de opción (input)
  let newOptionDiv = document.createElement("div");
  if (formType === 1) {
    newOptionDiv.innerHTML =
      '<input class="checkbox" type="checkbox"><input class="option" type="text" placeholder="Titulo opcion">';
  } else {
    newOptionDiv.innerHTML =
      '<li><input class="option" type="text" placeholder="Titulo opcion"></li>';
  }

  // Agregar el nuevo elemento al contenedor
  container.appendChild(newOptionDiv);
}
