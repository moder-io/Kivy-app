import webbrowser

def open_router_config_page():
    url = 'http://192.168.1.1'
    chrome_path = 'C:/Users/rfran/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe %s'
    webbrowser.get(chrome_path).open(url)

if __name__ == "__main__":
    open_router_config_page()
