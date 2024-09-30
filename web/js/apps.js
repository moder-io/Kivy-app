document.addEventListener("DOMContentLoaded", function() {
    const agregarAppButton = document.getElementById("agregarApp");
    const appsList = document.getElementById("rectangulo");

    const savedApps = JSON.parse(localStorage.getItem("userApps")) || [];
    savedApps.forEach(app => {
        agregarApp(app.url, app.imageUrl);
    });

    agregarAppButton.addEventListener("click", function() {
        const appUrlInput = document.getElementById("app-url");
        const appImageInput = document.getElementById("app-image");

        const url = appUrlInput.value;
        const imageUrl = appImageInput.value;

        if (url && imageUrl) {
            agregarApp(url, imageUrl);

            const savedApps = JSON.parse(localStorage.getItem("userApps")) || [];
            savedApps.push({ url, imageUrl });
            localStorage.setItem("userApps", JSON.stringify(savedApps));

            appUrlInput.value = "";
            appImageInput.value = "";
        }
    });

    function agregarApp(url, imageUrl) {
        const nuevaApp = document.createElement("a");
        nuevaApp.href = url;

        const nuevaImagen = document.createElement("img");
        nuevaImagen.src = imageUrl;
        nuevaImagen.className = "ico";

        nuevaApp.appendChild(nuevaImagen);
        appsList.appendChild(nuevaApp);

        nuevaApp.addEventListener("contextmenu", function(e) {
            e.preventDefault(); 

            const confirmarBorrar = confirm("¿Deseas borrar este enlace?");
            if (confirmarBorrar) {
                appsList.removeChild(nuevaApp);
                const savedApps = JSON.parse(localStorage.getItem("userApps")) || [];
                const index = savedApps.findIndex(app => app.url === url && app.imageUrl === imageUrl);
                if (index !== -1) {
                    savedApps.splice(index, 1);
                    localStorage.setItem("userApps", JSON.stringify(savedApps));
                }
            }
        });
    }
});