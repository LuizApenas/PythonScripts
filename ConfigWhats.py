from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

class SeleniumNavegador:

    def __init__(self):

        #CONFIG DO WEBDRIVER PARA NAVEGADOR COM WHASTAPP JÁ LOGADO
        self.options = webdriver.ChromeOptions()
        self.user_data_dir = r"C:\Users\OXXYGEN\AppData\Local\Google\Chrome\User Data\Default" #DIRETORIO DO PERIL DO GOOGLE
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_argument(f"user-data-dir={self.user_data_dir}")

        #WEB DRIVER DO GOOGLE COM CONFIGORAÇÕES DE PERFIL
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def abrirNavegador(self):
        
        url = "https://web.whatsapp.com/"
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(100) #TEMPO PARA LOGAR WHATS E DPS FECHAR O NAVEGADOR 
        self.driver.quit()

def main():
    navegador = SeleniumNavegador()
    navegador.abrirNavegador()

if __name__ == "__main__":
    main()

