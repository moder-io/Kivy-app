const form = document.getElementById('notas-form');
const textarea = document.getElementById('mensaje');
const notasContainer = document.getElementById('notas-recipiente'); 
const descargarBtn = document.getElementById('descargar-btn');
const savedText = localStorage.getItem('notas-text');
const savedNotes = JSON.parse(localStorage.getItem('notas-list')) || [];
const borrar = document.getElementById('borrar');

descargarBtn.addEventListener('click', () => {
  const fecha = new Date().toLocaleDateString();
  const nota = textarea.value + "\n";

  const titulo = "Fecha:" + new Date().toLocaleDateString() + "\n";
  const blank = "\n";
  const titulo2 = "Notas:";
  const contenido = titulo + blank + titulo2 + blank + textarea.value;
  localStorage.setItem('notas-text', textarea.value);
  const blob = new Blob([contenido], { type: 'text/plain' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'notas/recordatorios.txt';
  a.click();

  if (nota.trim() !== '') {
    const nuevaNota = {
      fecha: fecha,
      contenido: nota,
    };

    savedNotes.unshift(nuevaNota);

    if (savedNotes.length > 10) {
      savedNotes.pop();
    }
    localStorage.setItem('notas-list', JSON.stringify(savedNotes));
    textarea.value = '';
    cargarNotas();
  }
});

function cargarNotas() {
  notasContainer.innerHTML = '';
  savedNotes.forEach((nota, index) => {
    const notaDiv = document.createElement('div');
    notaDiv.classList.add('nota');
    notaDiv.innerHTML = `<strong>Fecha:</strong> ${nota.fecha}<br><strong>Notas:</strong> ${nota.contenido}`;
    
    notasContainer.appendChild(notaDiv);

    if (index < savedNotes.length - 1) {
      const hr = document.createElement('hr');
      notasContainer.appendChild(hr);
    }
  });
}

setInterval(cargarNotas, 10000);
cargarNotas()