from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
import pygetwindow
import re
import time
from pathlib import Path

#### EMAIL DO USUÁRIO ####
email = input("\n INSIRA SEU E-MAIL: \n")
regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
while not re.match(regex,email):
    print("email inválido !!!")
    email = input("\n INSIRA SEU E-MAIL: \n")

#### SENHA DO USUÁRIO ####
senha = input("\n INSIRA SUA SENHA: \n")
while not senha:
    print("a sua senha não pode ser nula !!!")
    senha = input("\n INSIRA SUA SENHA: \n")
#### EMAIL DO DESTINATARIO ####
email_destinatario = input("\n INSIRA O E-MAIL DO DESTINATARIO: \n")
while not re.match(regex,email_destinatario):
    print("email inválido !!!")
    email_destinatario = input("\n INSIRA O E-MAIL DO DESTINATARIO: \n")
#### ASSUNTO DO DESTINATARIO ####
assunto = input("\n INSIRA O ASSUNTO DO E-MAIL: \n")
while not assunto: 
    print("assunto não pode ser vazio !!!")
    assunto = input("\n INSIRA O ASSUNTO DO E-MAIL: \n")
#### MENSAGEM DO DESTINATARIO ####
mensagem = input("\n INSIRA A MENSAGEM DO E-MAIL: \n")
while not mensagem: 
    print("a mensagem não pode ser nula !!!")
    mensagem = input("\n INSIRA A MENSAGEM DO E-MAIL: \n")
#### QUANTIDADE DE ENVIOS DE EMAILS ####
quantidade_de_envios = input("\n QUANTAS VEZES QUER ENVIAR ESSA MENSAGEM AO DESTINATARIO ? \n")
while not quantidade_de_envios.isdigit():
    print("quantidade inválida !!!")
    quantidade_de_envios = input("\n QUANTAS VEZES QUER ENVIAR ESSA MENSAGEM AO DESTINATARIO ? \n")

#### CONFIGURAÇÃO DO CHROME (Options) ####
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--log-level=3")
#### CONFIGURANDO CAMINHO DO CHROMEDRIVER ####
pasta = Path("./chromedriver-win64/chromedriver-win64")
arquivo = "chromedriver.exe"
caminho = pasta / arquivo

servico = Service(str(caminho))

driver = webdriver.Chrome(service=servico , options=options)
#### LOGIN DO USUÁRIO ####
try: 
    driver.get("https://google.com/")
    
    while True:
        try:
            fazer_login = WebDriverWait(driver , 10).until(
                expected_conditions.element_to_be_clickable((By.CLASS_NAME , "gb_Ta"))
            )
            fazer_login.click()
            break
        except:
            pass


    email_input = WebDriverWait(driver , 10).until(
        expected_conditions.element_to_be_clickable((By.NAME , "identifier"))
    )

    email_input.click()

    email_input.send_keys(email)

    email_input.send_keys(Keys.ENTER)

    while True:
        try:
            email_invalido = WebDriverWait(driver , 10).until(
                expected_conditions.presence_of_element_located((By.XPATH , "//*[contains(text() , 'Não foi possível encontrar sua Conta do Google')]"))
            )
            if email_invalido:
                time.sleep(2)
                driver.minimize_window()
                print("\n \n #### EMAIL INCORRETO #### \n \n")
                email_valido = input("DIGITE SEU E-MAIL CORRIGIDO: ")
                while not email_valido or not re.match(regex,email_valido):
                    print("E-mail Vazio ou Inválido !!!")
                    email_valido = input("DIGITE SEU E-MAIL CORRIGIDO: ")
                driver.maximize_window()
                redigit_email = driver.find_element(By.NAME , "identifier")
                redigit_email.clear()
                redigit_email.click()
                redigit_email.send_keys(email_valido)
                redigit_email.send_keys(Keys.ENTER)

        except:
            driver.maximize_window()
            break

    senha_input = WebDriverWait(driver , 10).until(
        expected_conditions.element_to_be_clickable((By.NAME , "Passwd"))
    )

    senha_input.click()

    senha_input.send_keys(senha)

    senha_input.send_keys(Keys.ENTER)

    while True:
        try:
            senha_invalida = WebDriverWait(driver , 10).until(
                expected_conditions.presence_of_element_located((By.XPATH , "//*[contains(text() , 'Senha incorreta. Tente novamente ou clique em \"Esqueceu a senha?\" para escolher outra.')]"))
            )
            if senha_invalida:
                time.sleep(2)
                driver.minimize_window()
                print("\n \n #### SENHA INCORRETA #### \n \n")
                senha_valida = input("DIGITE SUA SENHA CORRIGIDA: ")
                while not senha_valida:
                    print("sua senha não pode ser nula !!!")
                    senha_valida = input("DIGITE SUA SENHA CORRIGIDA: ")
                driver.maximize_window()
                redigit_senha = driver.find_element(By.NAME , "Passwd")
                redigit_senha.clear()
                redigit_senha.send_keys(senha_valida)
                redigit_senha.send_keys(Keys.ENTER)
        except:
            driver.maximize_window()
            break

    while True:
        try:
            driver.find_element(By.ID , "APjFqb")
            break
        except:
            pass
    
    

    def send_email(destinatario,assunto,mensagem):
        driver.get("https://mail.google.com/mail/u/0/#inbox")
        while True:
            try: 
                compor = driver.find_element(By.XPATH , "//*[contains(text() , 'Compor')]")
                compor.click()
                break
            except:
                pass
        contador_move_to = 0
        while True:
            pyautogui.moveTo(500,500,duration=2)
            pyautogui.moveTo(600,500,duration=2)
            pyautogui.moveTo(700,500,duration=2)
            pyautogui.moveTo(800,500,duration=2)
            pyautogui.moveTo(900,500,duration=2)
            pyautogui.moveTo(1000,500,duration=2)
            pyautogui.moveTo(1100,500,duration=2)
            pyautogui.moveTo(1200,500,duration=2)
            pyautogui.moveTo(1300,500,duration=2)
            pyautogui.moveTo(1400,500,duration=2)
            pyautogui.moveTo(1500,500,duration=2)
            contador_move_to += 1
            if contador_move_to == 7:
                break

        while True:
            try: 
                Para = driver.find_element(By.CSS_SELECTOR , "input[aria-label='Para destinatários']")
                Para.click()
                Para.send_keys(destinatario)
                Para.send_keys(Keys.ENTER)
                Para.send_keys(Keys.TAB)
                break
            except:
                pass
        
        while True:
            try:
                Assunto = driver.find_element(By.CSS_SELECTOR , "input[aria-label='Assunto']")
                Assunto.click()
                Assunto.send_keys(assunto)
                Assunto.send_keys(Keys.ENTER)
                Assunto.send_keys(Keys.TAB)
                break
            except:
                pass

        while True:
            try:
                Mensagem = driver.find_element(By.CSS_SELECTOR , "div[aria-label='Corpo da Mensagem']")
                Mensagem.click()
                Mensagem.send_keys(mensagem)
                Mensagem.send_keys(Keys.ENTER)
                break
            except:
                pass
        
        pyautogui.hotkey("ctrl","enter")

        time.sleep(5)

        driver.get("https://google.com/")
        
    for enviar in range(int(quantidade_de_envios)):
        send_email(email_destinatario,assunto,mensagem)
        print(f"{enviar}° - Envio para o destinatario silvanapenhapires825@gmail.com")
except ValueError:
    print(f"error {ValueError}")

input("Desativar...")