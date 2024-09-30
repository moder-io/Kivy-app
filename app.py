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
        relative_path = 'web/index.html'
        current_dir = os.getcwd()
        absolute_path = os.path.join(current_dir, relative_path)
        file_url = 'file:///' + absolute_path.replace('\\', '/')
        brave_path = 'C:/Users/rfran/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe'
        webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
        webbrowser.get('brave').open(file_url)
        logger.info("Página web abierta")

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
     
    def popup2(self):
        popup = MiPopup2()
        popup.open()

    def ip_host(self):
        ruta_bat = 'red/ip o host.bat'
        os.system('start cmd /k "{}"'.format(ruta_bat))
        logger.info("ip_host ejecutado")

    def red(self):
        ruta_bat = 'red/red config.bat'
        os.system('start cmd /k "{}"'.format(ruta_bat))
        logger.info("gestor de red ejecutado")

    def exit(self):
        self.stop()


if __name__ == "__main__":
    app = MainApp()
    app.run()

logging.shutdown() 
