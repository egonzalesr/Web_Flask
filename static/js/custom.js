// get current year
(function () {
  var year = new Date().getFullYear();
  document.querySelector("#currentYear").innerHTML = year;
})();


// Función para desplazarse suavemente al inicio de la página
function scrollToTopSmooth() {
  const scrollDuration = 300; // en milisegundos
  const scrollStep = -window.scrollY / (scrollDuration / 15);

  const scrollInterval = setInterval(function () {
    if (window.scrollY !== 0) {
      window.scrollBy(0, scrollStep);
    } else {
      clearInterval(scrollInterval);
    }
  }, 15);
}

// Función para mostrar u ocultar el botón según la posición del scroll
window.onscroll = function () {
  var scrollToTopBtn = document.getElementById("scrollToTopBtn");

  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
};

// Agrega un evento de clic al botón para desplazarse suavemente al inicio
document.getElementById("scrollToTopBtn").addEventListener("click", scrollToTopSmooth);


// Validación de formulario
const $form = document.getElementById('contactForm');
const $name = document.getElementById('name');
const $email = document.getElementById('mail');
const $phone = document.getElementById('phone');
const $message = document.getElementById('message');


$phone.addEventListener('keypress', (event) => {
  event.preventDefault();
  let codigoKey = event.keyCode;
  let valorKey = String.fromCharCode(codigoKey);
  let telefonoActual = $phone.value;

  if (telefonoActual.length >= 0 && telefonoActual.length < 15) {
    if (!isNaN(valorKey) || valorKey === '0' || valorKey === '+') {
      $phone.value += valorKey;
    }
  }
});


$form.addEventListener('submit', (event) => {
  event.preventDefault();
  validateName($name.value)
  validateEmail($email.value)
  validatePhone($phone.value)
  validateMessage($message.value)

  if (formIsValid()) {
    Swal.fire({
      title: '¡Éxito!',
      text: 'Solicitud enviada con éxito',
      icon: 'success',
    });
    $name.value = "";
    $email.value = "";
    $phone.value = "";
    $message.value = "";
  } else {
    Swal.fire({
      title: '¡Error!',
      text: 'Todos los campos deben estár llenos',
      icon: 'error',
    });
  }
});

function validateName(name) {
  if (name.length == 0) {
    $name.classList.remove("validate-ok")
    $name.classList.add("validate-warning")
  } else {
    $name.classList.remove("validate-warning")
    $name.classList.add("validate-ok")
  }

}

function validateEmail(email) {
  let mailRegex = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g

  if (mailRegex.test(email) == true) {
    $email.classList.remove("validate-warning")
    $email.classList.add("validate-ok")
  } else {
    $email.classList.remove("validate-ok")
    $email.classList.add("validate-warning")
  }
}

function validatePhone(phone) {
  let phoneRegex = /^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$/gm

  if (phoneRegex.test(phone) == true) {
    $phone.classList.remove("validate-warning")
    $phone.classList.add("validate-ok")

  } else {
    $phone.classList.remove("validate-ok")
    $phone.classList.add("validate-warning")
  }
}

function validateMessage(message) {
  if (message.length == 0) {
    $message.classList.remove("validate-ok")
    $message.classList.add("validate-warning")
  } else {
    $message.classList.remove("validate-warning")
    $message.classList.add("validate-ok")
  }
}

function formIsValid() {
  return $name.classList.contains('validate-ok') &&
    $email.classList.contains('validate-ok') &&
    $phone.classList.contains('validate-ok') &&
    $message.classList.contains('validate-ok');
}