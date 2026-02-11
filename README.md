# Portal de Trabajo para Programadores

**Portal de Trabajo para Programadores** es una aplicación de escritorio desarrollada con **Kivy**, diseñada para centralizar el acceso a herramientas esenciales de desarrollo en un solo lugar.

Su objetivo es mejorar la productividad ofreciendo una interfaz clara, moderna e intuitiva desde la que abrir rápidamente utilidades como la terminal, PowerShell, Visual Studio Code o recursos web.

---

## Características

* **Interfaz intuitiva** basada en Material Design (KivyMD).
* **Acceso rápido a herramientas** de desarrollo comunes.
* **Tema oscuro** para una experiencia visual más cómoda.
* **Aplicación ligera** y de rápido arranque.
* **Arquitectura sencilla**, fácil de modificar y ampliar.
* **Sistema de logs** para registrar acciones importantes.

---

## Estructura del proyecto

```
project/
│
├── app.py
├── design.kv
├── images/
│   ├── background-popup.png
│   ├── github.png
│   ├── icon.png
│   ├── powershell.png
│   ├── terminal.png
│   └── visual.png
├── logs.log
└── README.md
```

---

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado:

* Python **3.10 o superior**
* pip

Instala las dependencias con:

```bash
pip install kivy kivymd
```

---

## Ejecución

Desde la carpeta del proyecto:

```bash
python app.py
```
O usar el ejecutable .exe en Releases.