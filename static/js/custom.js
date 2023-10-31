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
const $newsletter = document.getElementById('subscribeForm');
const $newsletterEmail = document.getElementById('SubscribeMail');
const $name = document.getElementById('name');
const $email = document.getElementById('mail');
const $phone = document.getElementById('phone');
const $message = document.getElementById('message');


$form.addEventListener('submit', function (event) {
  event.preventDefault();

  const overlay = document.getElementById('overlay');
  const loader = document.getElementById('loader');
  overlay.style.display = 'block';
  loader.style.display = 'block';

  if (!formIsValid()) {
    overlay.style.display = 'none';
    loader.style.display = 'none';
    Swal.fire({
      title: '¡Error!',
      text: 'Todos los campos deben estar completos',
      icon: 'error',
    });
    return;
  }

  fetch("/formulario_contacto", {
    method: "POST",
    body: new FormData($form),
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        Swal.fire({
          title: '¡Éxito!',
          text: 'Solicitud enviada con éxito',
          icon: 'success',
        });
        $name.value = "";
        $email.value = "";
        $phone.value = "";
        $message.value = "";
        overlay.style.display = 'none';
        loader.style.display = 'none';
      } else {
        Swal.fire({
          title: '¡Error!',
          text: 'No se pudo enviar el mensaje:' + data.error,
          icon: 'error',
        });
        overlay.style.display = 'none';
        loader.style.display = 'none';
      }
    })
    .catch(error => {
      console.error("Error:", error);
      overlay.style.display = 'none';
      loader.style.display = 'none';
    });
  $name.classList.remove("validate-ok")
  $email.classList.remove("validate-ok")
  $phone.classList.remove("validate-ok")
  $message.classList.remove("validate-ok")
});

$newsletter.addEventListener('submit', function (event) {
  event.preventDefault();
  const overlay = document.getElementById('overlay');
  const loader = document.getElementById('loader');
  overlay.style.display = 'block';
  loader.style.display = 'block';

  if (!$newsletterEmail.classList.contains('validate-ok')) {
    overlay.style.display = 'none';
    loader.style.display = 'none';
    Swal.fire({
      title: '¡Error!',
      text: 'Todos los campos deben estar completos',
      icon: 'error',
    });
    return;
  }
  fetch("/formulario_boletin", {
    method: "POST",
    body: new FormData($newsletter),
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        Swal.fire({
          title: '¡Éxito!',
          text: 'Te enviaremos noticias sobre nosotros',
          icon: 'success',
        });
        $newsletterEmail.value = "";
        overlay.style.display = 'none';
        loader.style.display = 'none';
      } else {
        Swal.fire({
          title: '¡Error!',
          text: 'No se pudo unir al boletín:' + data.error,
          icon: 'error',
        });
        overlay.style.display = 'none';
        loader.style.display = 'none';
      }
    })
    .catch(error => {
      console.error("Error:", error);
      overlay.style.display = 'none';
      loader.style.display = 'none';
    });
  $newsletterEmail.classList.remove("validate-ok")
});

$name.addEventListener('input', () => {
  if ($name.value.length == 0) {
    $name.classList.remove("validate-ok")
    $name.classList.add("validate-warning")
  } else {
    $name.classList.remove("validate-warning")
    $name.classList.add("validate-ok")
  }
})

$email.addEventListener('input', () => {
  let mailRegex = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g

  if (mailRegex.test($email.value) == true) {
    $email.classList.remove("validate-warning")
    $email.classList.add("validate-ok")
  } else {
    $email.classList.remove("validate-ok")
    $email.classList.add("validate-warning")
  }
})

$phone.addEventListener('input', (event) => {
  let phoneRegex = /^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$/gm;

  let codigoKey = event.data;

  if (phoneRegex.test($phone.value) == true) {
    $phone.classList.remove("validate-warning");
    $phone.classList.add("validate-ok");
  } else {
    $phone.classList.remove("validate-ok");
    $phone.classList.add("validate-warning");
  }

  if ($phone.value.length >= 0 && $phone.value.length < 15) {
    if (!isNaN(codigoKey) || codigoKey === '0' || codigoKey === '+') {
    } else {
      $phone.value = $phone.value.slice(0, -1);
    }
  }
});

$message.addEventListener('input', () => {
  if ($message.value.length == 0) {
    $message.classList.remove("validate-ok")
    $message.classList.add("validate-warning")
  } else {
    $message.classList.remove("validate-warning")
    $message.classList.add("validate-ok")
  }
})

$newsletterEmail.addEventListener('input', () => {
  let mailRegex = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g

  if (mailRegex.test($newsletterEmail.value) == true) {
    $newsletterEmail.classList.remove("validate-warning")
    $newsletterEmail.classList.add("validate-ok")
  } else {
    $newsletterEmail.classList.remove("validate-ok")
    $newsletterEmail.classList.add("validate-warning")
  }
})

function formIsValid() {
  return $name.classList.contains('validate-ok') &&
    $email.classList.contains('validate-ok') &&
    $phone.classList.contains('validate-ok') &&
    $message.classList.contains('validate-ok');
}