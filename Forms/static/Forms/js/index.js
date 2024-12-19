/* FUNCION PARA MENU INICIAL DE  TARJETS INDEX */
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




//FUNCION PARA MODAL EMERGENTE
// Obtener el modal
var modal = document.getElementById("myModal");

// Obtener el botón que abre el modal
var btn = document.getElementById("openModalBtn");

// Obtener el elemento <span> que cierra el modal
var span = document.getElementsByClassName("close")[0];

// Cuando el usuario hace clic en el botón, abrir el modal
btn.onclick = function () {
    modal.style.display = "block";
}

// Cuando el usuario hace clic en <span> (x), cerrar el modal
span.onclick = function () {
    modal.style.display = "none";
}

// Cuando el usuario hace clic fuera del modal, también cerrarlo
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}






