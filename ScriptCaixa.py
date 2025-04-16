import tkinter as tk
from tkinter import ttk, messagebox
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import threading

class SeleniumNavegador:
    
    def __init__(self):
        self.is_visible = False
        self.configure_options()
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=self.options)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao iniciar o navegador: {str(e)}")
            raise e

    def configure_options(self, headless=True):
        """Configura as opções do Chrome"""
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--user-data-dir=C:/Users/zluiz/OneDrive/Área de Trabalho/ECV UBERLÂNDIA/PerfilGoogle")
        self.options.add_argument("--profile-directory=Profile 1")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-gpu")
        if headless:
            self.options.add_argument("--headless")

    def toggle_visibility(self):
        """Alterna a visibilidade do navegador"""
        try:
            current_url = self.driver.current_url
            self.driver.quit()
            
            # Reconfigura as opções com o novo estado de visibilidade
            self.is_visible = not self.is_visible
            self.configure_options(headless=not self.is_visible)
            
            # Reinicia o navegador
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=self.options)
            self.driver.get(current_url)
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao alternar visibilidade do navegador: {str(e)}")
            return False

    def abrirNavegador(self):
        url = "https://gestaoclick.com/login"
        self.driver.get(url)
        time.sleep(5)
    
    def fazerLogin(self):
        try:
            email = 'isovistoriascentro@gmail.com'
            senha = 'isocentro625'
            elemento_email = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/div/div[2]/div/div/div/form/div[2]/div[1]/div/input')
            elemento_email.send_keys(email)
            time.sleep(2)
            elemento_senha = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/div/div[2]/div/div/div/form/div[2]/div[2]/div/div/div/input')
            elemento_senha.send_keys(senha)
            time.sleep(2)
            elemento_botao = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/div/div[2]/div/div/div/form/div[3]/button')
            elemento_botao.click()
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return False
    
    def desLogar(self):
        try:
            elemento_lateral = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/header/nav/div/ul/li[3]/div[1]/div/img')
            elemento_lateral.click()
            time.sleep(1)
            elemento_logout = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/header/nav/div/ul/li[3]/div[2]/div[2]/div/div[3]/button')
            elemento_logout.click()
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Erro ao fazer logout: {e}")
            return False
        
    def lancamento_dia_pix(self, campo_infos_text):
        try:
            self.driver.get('https://gestaoclick.com/vendas_servicos/adicionar?retorno=%2Fvendas_servicos%2F%3Fmenu%3DMTE%3D')
            time.sleep(3)
            cliente = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[2]/div[2]/div/div[2]/div/span/input')
            cliente.click()
            cliente.send_keys('PARTICULAR')
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(5)
            servico = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[3]/div[2]/div[2]/div/div/table/tbody/tr/td[1]/div/span/input')
            servico.click()
            servico.send_keys('VISTORIA DE VEICULO')
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(3)

            forma_pgm = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[7]/div[2]/span/div[1]/div[1]')
            forma_pgm.click()
            time.sleep(3)
            metodo_pgm = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[7]/div[2]/div[2]/div/table/tr[2]/td[3]/div/span/input')
            metodo_pgm.click()
            metodo_pgm.send_keys('PIX/TRANSFERENCIA')
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(3)

            campo_infos = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[9]/div[1]/div/div[2]/textarea')
            campo_infos.send_keys(campo_infos_text)
            time.sleep(3)
            elemento_finalizar = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[10]/button')
            elemento_finalizar.click()
            time.sleep(3)
            
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao fazer lançamento PIX: {str(e)}")
            return False

    def lancamento_dia_dinheiro(self, campo_infos_text, valor_pago):
        try:
            self.driver.get('https://gestaoclick.com/vendas_servicos/adicionar?retorno=%2Fvendas_servicos%2F%3Fmenu%3DMTE%3D')
            time.sleep(3)
            cliente = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[2]/div[2]/div/div[2]/div/span/input')
            cliente.click()
            cliente.send_keys('PARTICULAR')
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(5)
            servico = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[3]/div[2]/div[2]/div/div/table/tbody/tr/td[1]/div/span/input')
            servico.click()
            servico.send_keys('VISTORIA DE VEICULO')
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(3)

            forma_pgm = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[7]/div[2]/span/div[1]/div[1]')
            forma_pgm.click()
            time.sleep(3)
            metodo_pgm = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[7]/div[2]/div[2]/div/table/tr[2]/td[3]/div/span/input')
            metodo_pgm.click()
            metodo_pgm.send_keys('DINHEIRO A VISTA')
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(3)

            pgm_dinheiro = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[3]/div[2]/div[2]/div/div/table/tbody/tr/td[4]/input')
            pgm_dinheiro.click()
            pgm_dinheiro.send_keys(valor_pago)
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(3)

            campo_infos = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[9]/div[1]/div/div[2]/textarea')
            campo_infos.send_keys(campo_infos_text)
            time.sleep(3)
            elemento_finalizar = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/aside[2]/div/section[2]/span/div[10]/button')
            elemento_finalizar.click()
            time.sleep(3)

            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao fazer lançamento DINHEIRO: {str(e)}")
            return False

class AplicacaoGestaoClick:
    def __init__(self):
        self.navegador = None
        self.root = tk.Tk()
        self.root.title("Lançamentos GestãoClick")
        self.root.geometry("500x500")  # Aumentei a altura para garantir espaço para todos os elementos
        self.root.resizable(False, False)
        self.configurar_interface()
        
        # Inicia o navegador automaticamente ao abrir a aplicação
        self.root.after(100, self.iniciar_navegador_thread)
        
    def configurar_interface(self):
        # Frame principal com padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="Sistema de Lançamentos GestãoClick", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Frame para botões de navegador
        nav_frame = ttk.Frame(main_frame)
        nav_frame.pack(fill=tk.X, pady=5)
        
        self.botao_navegador = ttk.Button(nav_frame, text="Mostrar Navegador", command=self.toggle_navegador, state=tk.DISABLED)
        self.botao_navegador.pack(side=tk.LEFT, padx=5)
        
        # Frame para botões de login/logout
        auth_frame = ttk.Frame(main_frame)
        auth_frame.pack(fill=tk.X, pady=5)
        
        self.botao_login = ttk.Button(auth_frame, text="Fazer Login", command=self.fazer_login, state=tk.DISABLED)
        self.botao_login.pack(side=tk.LEFT, padx=5)
        
        self.botao_logout = ttk.Button(auth_frame, text="Fazer Logout", command=self.fazer_logout, state=tk.DISABLED)
        self.botao_logout.pack(side=tk.LEFT, padx=5)
        
        # Frame para o formulário
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Opção de métodos de pagamento
        ttk.Label(form_frame, text="Método de Pagamento:").pack(anchor="w", pady=5)
        
        self.metodo_var = tk.StringVar(value="pix")
        
        payment_frame = ttk.Frame(form_frame)
        payment_frame.pack(fill=tk.X, pady=5)
        
        ttk.Radiobutton(payment_frame, text="PIX/Transferência", variable=self.metodo_var, value="pix", command=self.toggle_valor_entry).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(payment_frame, text="Dinheiro à Vista", variable=self.metodo_var, value="dinheiro", command=self.toggle_valor_entry).pack(side=tk.LEFT, padx=10)
        
        # Frame para o valor em dinheiro
        self.valor_frame = ttk.Frame(form_frame)
        self.valor_frame.pack(fill=tk.X, pady=5)
        ttk.Label(self.valor_frame, text="Valor (R$):").pack(side=tk.LEFT, padx=5)
        self.valor_entry = ttk.Entry(self.valor_frame, width=10)
        self.valor_entry.pack(side=tk.LEFT, padx=5)
        self.valor_entry.config(state=tk.DISABLED)
        
        # Campo de informações
        ttk.Label(form_frame, text="Informações do Lançamento:").pack(anchor="w", pady=5)
        self.info_text = tk.Text(form_frame, height=8, width=50, wrap=tk.WORD)
        self.info_text.pack(pady=5)
        
        # Frame para botões de ação
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=tk.X, pady=10)
        
        # Botão de lançamento
        self.botao_lancamento = ttk.Button(action_frame, text="Realizar Lançamento", command=self.realizar_lancamento)
        self.botao_lancamento.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # Botão de sair
        self.botao_sair = ttk.Button(action_frame, text="Sair", command=self.sair_aplicacao)
        self.botao_sair.pack(side=tk.RIGHT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Iniciando navegador...")
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def iniciar_navegador_thread(self):
        """Inicia o navegador em uma thread separada para não bloquear a interface"""
        threading.Thread(target=self.iniciar_navegador, daemon=True).start()
        
    def iniciar_navegador(self):
        try:
            self.status_var.set("Iniciando navegador... Por favor, aguarde.")
            self.root.update()
            
            self.navegador = SeleniumNavegador()
            self.navegador.abrirNavegador()
            
            self.status_var.set("Navegador iniciado! Use o botão 'Fazer Login' para acessar o sistema.")
            # Habilita os botões
            self.root.after(0, lambda: self.botao_login.config(state=tk.NORMAL))
            self.root.after(0, lambda: self.botao_navegador.config(state=tk.NORMAL))
                
        except Exception as e:
            self.status_var.set(f"Erro ao iniciar navegador: {str(e)}")
            messagebox.showerror("Erro", f"Ocorreu um erro ao iniciar o navegador: {str(e)}")
    
    def fazer_login(self):
        """Função para o botão de login"""
        if not self.navegador:
            messagebox.showerror("Erro", "O navegador não está iniciado!")
            return
            
        self.status_var.set("Fazendo login... Por favor, aguarde.")
        self.root.update()
        
        def login_thread():
            if self.navegador.fazerLogin():
                self.status_var.set("Login realizado com sucesso!")
                # Habilita apenas o botão de logout após o login bem-sucedido
                # Botão de lançamento permanece sempre ativo
                self.root.after(0, lambda: self.botao_logout.config(state=tk.NORMAL))
                self.root.after(0, lambda: self.botao_login.config(state=tk.DISABLED))
            else:
                self.status_var.set("Falha ao realizar login. Verifique as credenciais.")
                messagebox.showerror("Erro", "Falha ao realizar login. Verifique as credenciais ou tente novamente.")
        
        threading.Thread(target=login_thread, daemon=True).start()
    
    def fazer_logout(self):
        """Função para o botão de logout"""
        if not self.navegador:
            messagebox.showerror("Erro", "O navegador não está iniciado!")
            return
            
        self.status_var.set("Fazendo logout... Por favor, aguarde.")
        self.root.update()
        
        def logout_thread():
            try:
                if self.navegador.desLogar():
                    self.status_var.set("Logout realizado com sucesso")
                    # Atualiza o estado dos botões após o logout bem-sucedido
                    # Botão de lançamento permanece sempre ativo
                    self.root.after(0, lambda: self.botao_logout.config(state=tk.DISABLED))
                    self.root.after(0, lambda: self.botao_login.config(state=tk.NORMAL))
                    
                    # Volta para a página de login
                    self.navegador.abrirNavegador()
                else:
                    self.status_var.set("Falha ao fazer logout")
            except Exception as e:
                self.status_var.set(f"Erro ao fazer logout: {str(e)}")
        
        threading.Thread(target=logout_thread, daemon=True).start()
        
    def toggle_valor_entry(self):
        """Habilita ou desabilita o campo de valor baseado no método de pagamento selecionado"""
        if self.metodo_var.get() == "dinheiro":
            self.valor_entry.config(state=tk.NORMAL)
        else:
            self.valor_entry.config(state=tk.DISABLED)
            self.valor_entry.delete(0, tk.END)
        
    def realizar_lancamento(self):
        if not self.navegador:
            messagebox.showerror("Erro", "O navegador não está iniciado!")
            return
        
        campo_infos_text = self.info_text.get("1.0", tk.END).strip()
        if not campo_infos_text:
            messagebox.showerror("Erro", "O campo de informações não pode estar vazio!")
            return
        
        metodo = self.metodo_var.get()
        self.status_var.set(f"Realizando lançamento via {metodo.upper()}...")
        self.root.update()
        
        def lancamento_thread():
            resultado = False
            
            try:
                # Verifica se o usuário está logado antes de realizar o lançamento
                current_url = self.navegador.driver.current_url
                if "login" in current_url:
                    self.status_var.set("Usuário não logado. Tentando fazer login automático...")
                    if not self.navegador.fazerLogin():
                        self.status_var.set("Falha ao fazer login automático. Realize o login manualmente.")
                        messagebox.showwarning("Aviso", "Usuário não logado. Por favor, faça o login antes de realizar o lançamento.")
                        return
                    
                # Continua com o lançamento
                if metodo == "pix":
                    resultado = self.navegador.lancamento_dia_pix(campo_infos_text)
                elif metodo == "dinheiro":
                    valor_pago = self.valor_entry.get().strip()
                    if not valor_pago:
                        messagebox.showerror("Erro", "O campo de valor não pode estar vazio para pagamento em dinheiro!")
                        return
                    try:
                        # Substitui ponto por vírgula se houver
                        valor_pago = valor_pago.replace('.', ',')
                        resultado = self.navegador.lancamento_dia_dinheiro(campo_infos_text, valor_pago)
                    except ValueError:
                        messagebox.showerror("Erro", "O valor deve ser um número válido!")
                        return
                
                if resultado:
                    self.status_var.set("Lançamento realizado com sucesso")
                    self.root.after(0, lambda: self.info_text.delete("1.0", tk.END))
                    
                    def perguntar_continuar():
                        continuar = messagebox.askyesno("Sucesso", "Lançamento realizado com sucesso! Deseja realizar outro lançamento?")
                        if not continuar:
                            # Não precisa mais perguntar sobre logout, já que temos um botão específico para isso
                            pass
                    
                    self.root.after(0, perguntar_continuar)
                else:
                    self.status_var.set("Falha ao realizar lançamento")
            except Exception as e:
                self.status_var.set(f"Erro ao realizar lançamento: {str(e)}")
                messagebox.showerror("Erro", f"Ocorreu um erro ao realizar o lançamento: {str(e)}")
        
        threading.Thread(target=lancamento_thread, daemon=True).start()
    
    def sair_aplicacao(self):
        if self.navegador:
            try:
                self.navegador.driver.quit()
            except:
                pass
        self.root.destroy()
    
    def toggle_navegador(self):
        """Alterna a visibilidade do navegador"""
        if not self.navegador:
            messagebox.showerror("Erro", "O navegador não está iniciado!")
            return
            
        self.status_var.set("Alternando visibilidade do navegador...")
        self.root.update()
        
        def toggle_thread():
            if self.navegador.toggle_visibility():
                if self.navegador.is_visible:
                    self.status_var.set("Navegador visível")
                    self.root.after(0, lambda: self.botao_navegador.config(text="Esconder Navegador"))
                else:
                    self.status_var.set("Navegador oculto")
                    self.root.after(0, lambda: self.botao_navegador.config(text="Mostrar Navegador"))
            else:
                self.status_var.set("Erro ao alternar visibilidade do navegador")
        
        threading.Thread(target=toggle_thread, daemon=True).start()
    
    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AplicacaoGestaoClick()
    app.iniciar()