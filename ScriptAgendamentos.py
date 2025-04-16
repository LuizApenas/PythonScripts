from argparse import Action
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumNavegador:

    def __init__(self):

        #CONFIG DO WEBDRIVER PARA NAVEGADOR COM WHASTAPP JÁ LOGADO
        self.options = webdriver.ChromeOptions()
        self.user_data_dir = r"C:\Users\OXXYGEN\AppData\Local\Google\Chrome\User Data\Default" #DIRETORIO DO PERIL DO GOOGLE
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_argument(f"user-data-dir={self.user_data_dir}")
        
        #TESTE NA MAQUINA LUIZ
        #self.options.add_argument("--user-data-dir=****")
        #self.options.add_argument("--profile-directory=Profile 1") # Default é o perfil principal
        
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--disable-software-rasterizer')
        self.options.add_argument('--disable-dev-tools')
        self.options.add_argument('--no-first-run')
        self.options.add_argument('--no-default-browser-check')
        self.options.add_argument('--disable-popup-blocking')
        self.options.add_argument('--disable-notifications')
    
        self.options.add_argument("--headless")
    
        #WEB DRIVER DO GOOGLE COM CONFIGORAÇÕES DE PERFIL
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        
    def abrirNavegador(self):
        
        url = 'https://google.com/'
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(5)
    
    def fazerLogin(self):
        
        #SITE DOS AGENDAMENTOS 
        url = 'https://agendamento.prodemge.gov.br/ssc/login/login'
        self.driver.get(url)
        time.sleep(15)

        login = "*"
        elemento_login = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[3]/div[3]/div/div[2]/div/form/div[1]/input")
        elemento_login.send_keys(login)
        time.sleep(3)

        senha = "*"
        elemento_senha = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[3]/div[3]/div/div[2]/div/form/div[2]/div[1]/input")
        elemento_senha.send_keys(senha)
        time.sleep(3)

        elemento_botao = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[3]/div[3]/div/div[2]/div/form/div[4]/button[2]")
        elemento_botao.click()
        time.sleep(10)
        
    def agendamentosDia(self):
 
        #SELECIONA A UNIDADE DE ATENDIMENTO
        elemento_unidade = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/div[2]/select")
        elemento_unidade.click()
        time.sleep(3)
        elemento_unidade.send_keys("ECV")
        time.sleep(3)

        #CLICA EM OK
        elemento_unidadeOK = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/button/span")
        elemento_unidadeOK.click()
        time.sleep(5)
        actions = ActionChains(self.driver)
        #ENTRA NA PAGINA DOS AGENDAMENTOS E FAZ ALGUMAS CONFIGURAÇÕES PARA ENQUADRAR OS AGENDAMENTOS PARA O PRINT
        self.driver.get('https://agendamento.prodemge.gov.br/relatorios/relatorio_agendamentos_dia')
        #self.driver.execute_script("document.body.style.zoom='90%'")
        self.driver.maximize_window()
        time.sleep(10)
        actions.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)

    def printTelaEnvio(self):
        
        #TIRA O PRINT DA TELA COM OS AGENDAMENTOS E SALVA
        
        time.sleep(5)
        screenshot_path = r"C:\Users\OXXYGEN\Downloads\screenshot.png"
        self.driver.save_screenshot(screenshot_path)
        
        fazerLogout = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[3]/div[2]/ul/li[3]/a")
        fazerLogout.click()
        
        #ENTRA NO WHATSAPP WEB JÁ LOGADO PELO PERFIL DO GOOGLE
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(50)  # TEMPO PARA CARREGAR O WHATSAPP
        #self.driver.execute_script("document.body.style.zoom='100%'")
        
        #BUSCA O GRUPO
        grupo = "ISO VISTORIAS CENTRO"
        buscar_conversa = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[3]/div/div[1]/div/div[2]/div/div/div/p")
        buscar_conversa.click()
        buscar_conversa.send_keys(grupo)
        time.sleep(5)
        buscar_conversa.send_keys(Keys.ENTER)

        #PEGA DATA E HORARIO PARA ENVIAR NO CORPO DA MSG
        agora = datetime.now()
        dia = agora.strftime("%d/%m/%Y")
        hora = agora.strftime("%H:%M:%S")
        conteudo_msg = f"Agendamento Automático do dia {dia}, às {hora}."
        time.sleep(5)

        #CLICA NO CORPO DA MSG
        corpo_msg = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p")
        corpo_msg.click()
        corpo_msg.send_keys(conteudo_msg)
        time.sleep(5)

        #BUSCA O CLIP DE ANEXO NO WHATSAPP
        time.sleep(5)
        botao_anexo = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[1]/div/button/span")
        botao_anexo.click()

        #SELECIONA O ENVIO DO PRINT
        time.sleep(5)
        envio_imagem = self.driver.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
        envio_imagem.send_keys(screenshot_path)
        time.sleep(5)

        #ENVIA A MSG
        botao_enviar = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span")
        botao_enviar.click()
        time.sleep(5)
        
        #FECHA WEBDRIVER / NAVEGADOR
        self.driver.quit()

def main():
    
    navegador = SeleniumNavegador()
    
    navegador.abrirNavegador()
    navegador.fazerLogin()
    navegador.agendamentosDia()
    navegador.printTelaEnvio()

if __name__ == "__main__":
    main()
