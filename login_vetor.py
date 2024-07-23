from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import pyautogui as auto
from unidecode import unidecode
import pyperclip
import datetime
import os

teste = False

 
def aguardar_elemento(class_name,tempo_maximo_espera = 10,by = By.CLASS_NAME):
    # Espera até que o elemento desejado esteja presente na página
    try:
        elemento = WebDriverWait(driver, tempo_maximo_espera).until(
            EC.presence_of_element_located((By.CLASS_NAME, f"{class_name}")))
        time.sleep
        print("A página carregou com sucesso!")
    except Exception as e:
        print("Erro: A página não carregou dentro do tempo especificado.")
        driver.stop_casting() #parar programa.
  
df_log = pd.DataFrame()
driver = webdriver.Edge()
 
def programa():
    df_atendimentos = pd.read_excel(file)
    #Leitura de login e senha
    for index, row in df_atendimentos.iterrows():
        logon = df_atendimentos.iloc[0]['LOGIN']
        senha = df_atendimentos.iloc[0]['SENHA']
    if teste == True:
        link_login = "https://gtfhmg.vamoslocacao.com.br/master/login.php"
    else:
        link_login = "https://gtf.vamoslocacao.com.br/login.php"
    driver.get(link_login)

    #Login do usuário
    driver.execute_script(f'document.getElementsByClassName("form-control-login").logon.value = "{logon}"')
    driver.execute_script(f'document.getElementsByClassName("form-control-login").senha.value = "{senha}"')
    driver.execute_script(f'document.getElementsByClassName("btn btn-submit btn-block g-recaptcha")[2].click()')
    #Aguarda login
    aguardar_elemento("i_menu")
 
#Cérebro do programa
diretorio = (r"C:\Users\igor.gabriel\OneDrive - JSL SA\Área de Trabalho\AUTOMAÇÃO IMPLANTAÇÃO\Planilhas")
d= os.listdir(diretorio)
for filename in d:
        print(f"arquivos do diretorio {d}")
        print(f'lendo {filename}')
        if filename.endswith('.xlsx'):
            file = os.path.join(diretorio, filename)
            programa()
print('FIM')
time.sleep(10)
#driver.quit()