// get current year
(function () {
    var year = new Date().getFullYear();
    document.querySelector("#currentYear").innerHTML = year;
})();


// Función para desplazarse suavemente al inicio de la página
function scrollToTopSmooth() {
    const scrollDuration = 300; // en milisegundos
    const scrollStep = -window.scrollY / (scrollDuration / 15);
    
    const scrollInterval = setInterval(function() {
      if (window.scrollY !== 0) {
        window.scrollBy(0, scrollStep);
      } else {
        clearInterval(scrollInterval);
      }
    }, 15);
  }
  
  // Función para mostrar u ocultar el botón según la posición del scroll
  window.onscroll = function() {
    var scrollToTopBtn = document.getElementById("scrollToTopBtn");
    
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      scrollToTopBtn.style.display = "block";
    } else {
      scrollToTopBtn.style.display = "none";
    }
  };
  
  // Agrega un evento de clic al botón para desplazarse suavemente al inicio
  document.getElementById("scrollToTopBtn").addEventListener("click", scrollToTopSmooth);  