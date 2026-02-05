from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import Popup
import webbrowser, logging, os, sys


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


class MainApp(MDApp):
    title = "App"

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS  # PyInstaller
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


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
        os.system("code .")
        logger.info("Visual Studio Code abierto")


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.icon = self.resource_path("images/icon.png")
        Builder.load_file(self.resource_path("design.kv"))
        return Ui() 


    def popup(self):
        popup = MiPopup()
        popup.open()
        logger.info("popup abierto")


    def exit(self): 
        self.stop()


if __name__ == "__main__":
    app = MainApp()
    app.run()


logging.shutdown() 