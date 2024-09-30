const textSizeSelect = document.getElementById('text-size-select');
const applySettingsButton = document.getElementById('apply-settings');
const exitSettingsButton = document.getElementById('exit-settings');
const toggleSettings = document.getElementById('toggle-settings');
const settingsContent = document.querySelector('.settings-content');
const barraLateral = document.querySelector('.barra-lateral');
const ladoBarraLateral = document.getElementById('lado-barra-lateral');
const barraLateral1 = document.querySelector('.barra-lateral1');
const barraLateral2 = document.querySelector('.barra-lateral2');
const header = document.querySelector('.mi-header');
const footer = document.querySelector(".mi-footer");
const mostrar = document.getElementById("mostrar")
const widjetTiempo = document.getElementById("weather")
const diamante = document.getElementById('objeto')

function applyStyles(selectedTextSize, mostar) {

    switch (selectedTextSize) {
        case 'small':
            document.body.style.fontSize = '14px';
            break;
        case 'medium':
            document.body.style.fontSize = '16px';
            break;
        case 'large':
            document.body.style.fontSize = '18px';
            break;
    }

    switch (mostar) {
        case "si":
            widjetTiempo.style.visibility = "visible";
            break;
        case "no":
            widjetTiempo.style.visibility = "hidden";
            break;
    }
}
setInterval(applyStyles, 10000);
applyStyles();


applySettingsButton.addEventListener('click', () => {
    const selectedTextSize = textSizeSelect.value;
    const mostar1 = mostrar.value;

    applyStyles(selectedTextSize, mostar1);

    localStorage.setItem('selectedTextSize', selectedTextSize);
    localStorage.setItem('mostar', mostar1);
});

window.addEventListener('load', () => {
    const savedTextSize = localStorage.getItem('selectedTextSize') || 'medium';
    const savedMostrar = localStorage.getItem('mostar') || 'si';

    textSizeSelect.value = savedTextSize;
    mostrar.value = savedMostrar;

    applyStyles(savedTextSize, savedMostrar);
});

exitSettingsButton.addEventListener('click', () => {
    settingsContent.style.display = 'none';
});

toggleSettings.addEventListener('click', () => {
    if (settingsContent.style.display === 'block') {
        settingsContent.style.display = 'none';
    } else {
        settingsContent.style.display = 'block';
    }
});





window.onload = function () {
    var enlacesGuardados = JSON.parse(localStorage.getItem('enlaces')) || [];

    if (enlacesGuardados.length > 0) {
        var ul = document.getElementById('enlaces-lista');

        enlacesGuardados.forEach(function (enlace) {
            var li = document.createElement('li');
            var a = document.createElement('a');
            var img = document.createElement('img');

            a.href = enlace.url;
            img.src = enlace.icono;
            img.className = 'ico-barralateral';
            li.className = 'enlace-barralateral';

            a.appendChild(img);
            li.appendChild(a);
            ul.appendChild(li);
        });
    }
};

function agregarEnlace() {
    var nuevoEnlace = document.getElementById('nuevo-enlace').value;
    var nuevoIcono = document.getElementById('nuevo-icono').value;

    if (nuevoEnlace && nuevoIcono) {
        var ul = document.getElementById('enlaces-lista');
        var li = document.createElement('li');
        var a = document.createElement('a');
        var img = document.createElement('img');

        a.href = nuevoEnlace;
        img.src = nuevoIcono;
        img.className = 'ico-barralateral';

        a.appendChild(img);
        li.appendChild(a);
        ul.appendChild(li);

        var enlacesGuardados = JSON.parse(localStorage.getItem('enlaces')) || [];
        enlacesGuardados.push({ url: nuevoEnlace, icono: nuevoIcono });
        localStorage.setItem('enlaces', JSON.stringify(enlacesGuardados));

        document.getElementById('nuevo-enlace').value = '';
        document.getElementById('nuevo-icono').value = '';
    }
}

function borrarEnlace() {
    var ul = document.getElementById('enlaces-lista');
    ul.innerHTML = '';
    localStorage.setItem('enlaces', '[]');
}




const contenedorDireccion = document.querySelector('.contenedor-direccion');
const contenedorBoton = document.querySelector('.contenedor-boton');
let visible = false;

contenedorBoton.addEventListener('click', function(e) {
    e.preventDefault();
    if (visible) {
        contenedorDireccion.style.visibility = 'hidden';
        visible = false;
    } else {
        contenedorDireccion.style.visibility = 'visible';
        visible = true;
    }
})
