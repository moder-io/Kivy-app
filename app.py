from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, RiseInTransition
from kivy.lang import Builder
from kivy.uix.popup import Popup
import webbrowser
import subprocess
import logging
import os

logging.basicConfig(filename='logs.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

class Ui(ScreenManager):
    pass

class WelcomePopup(Popup):
    pass

class MainApp(MDApp):
    icon = "images/icon.png"
    title = "Enhanced App"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file("design.kv")

    def on_start(self):
        self.show_welcome_popup()

    def show_welcome_popup(self):
        popup = WelcomePopup()
        popup.open()
        logging.info("Welcome popup opened")

    def run_script(self, script_name):
        script_path = os.path.join("scripts", f"{script_name}.py")
        subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f'User ran {script_name} script')

    def open_terminal(self, terminal_type):
        os.system(f"start {terminal_type}")
        logging.info(f"{terminal_type} opened")

    def open_website(self, url):
        webbrowser.open(url)
        logging.info(f"Opened website: {url}")

    def open_application(self, app_path):
        os.system(f'start "" "{app_path}"')
        logging.info(f"Opened application: {app_path}")

    def exit_app(self):
        self.stop()

if __name__ == "__main__":
    MainApp().run()