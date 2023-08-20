from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from password import mail, site, senha

def cadastro_web(dataframe):

    # realizando login no sistema
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(site)

    email = browser.find_element(By.XPATH, '//*[@id="email"]')
    email.send_keys(mail)

    login = browser.find_element(By.XPATH, '//*[@id="password"]')
    login.send_keys(senha)

    time.sleep(1)

    button = browser.find_element(By.XPATH, '//*[@id="submit"]')
    button.click()

    time.sleep(3)

    #iterando sobre as linhas do dataframe
    # iterrows retorna uma tupla
    # _ é para descartar o indice da tupla
    for _, linha in dataframe.iterrows():
        cliente = browser.find_element(By.XPATH, '//*[@id="nome"]')
        cliente.send_keys(linha['Nome'])

        email = browser.find_element(By.XPATH, '//*[@id="email"]')
        email.send_keys(linha['E-mail'])

        telefone = browser.find_element(By.XPATH, '//*[@id="telefone"]')
        telefone.send_keys(linha['Telefone'])

        cidade = browser.find_element(By.XPATH, '//*[@id="cidade"]')
        cidade.send_keys(linha['Cidade'])

        estado = browser.find_element(By.XPATH, '//*[@id="estado"]')
        estado.send_keys(linha['Estado'])

        time.sleep(3)

        botao_cadastra = browser.find_element(By.XPATH, '//*[@id="submit"]')
        botao_cadastra.click()

    browser.close()




