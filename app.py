import os
import sys
from pathlib import Path


if sys.platform.startswith("win"):
    base = Path(os.getenv("LOCALAPPDATA", Path.home()))
    os.environ["KIVY_HOME"] = str(base / "App")
else:
    os.environ["KIVY_HOME"] = str(Path.home() / ".App")


from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import Popup
import webbrowser, logging


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
        base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
        return str(base_path / relative_path)

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
