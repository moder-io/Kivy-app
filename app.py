from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import Popup
import webbrowser, subprocess, logging, os

logger = logging.getLogger() 
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs.log')
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Ui(ScreenManager): 
    pass

class MiPopup(Popup):
    pass

class MiPopup2(Popup):
    pass


class MainApp(MDApp):

    icon = "images/icon.png"
    title = "App"

    def encript(self):
        ruta_script = "encriptador/encriptador.py"
        subprocess.Popen(["python", ruta_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info('Usuario encripto')

    def desencript(self):
        ruta_script = "encriptador/desencriptar.py"
        subprocess.Popen(["python", ruta_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info('Usuario desencripto')

    def terminal(self):
       os.system("start cmd.exe")
       logger.info("Terminal abierto")

    def powerShell(self):
       os.system("start powershell.exe")
       logger.info("Power Shell abierto")

    def webOpen(self):
        url = "https://github.com"
        webbrowser.open(url)
        logger.info("github abierto")

    def visual(self):
        code_path = "C:/Users/rfran/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        os.system(f'start "" "{code_path}"')
        logger.info("Visual Studio Code abierto")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        Builder.load_file("desing.kv")
        return Ui() 

    def popup(self):
        popup = MiPopup()
        popup.open()
        logger.info("popup abierto")
     
    def popup2(self):
        popup = MiPopup2()
        popup.open()
        logger.info("popup2 abierto")

    def exit(self):
        self.stop()


if __name__ == "__main__":
    app = MainApp()
    app.run()

logging.shutdown() 