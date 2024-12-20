import pyautogui as p
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

texto = p.prompt('Digite um nick:')

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

chrome = webdriver.Chrome(options=options)

chrome.maximize_window()
chrome.get("https://www.op.gg/")
chrome.find_element(By.ID, "searchHome").send_keys(texto)
chrome.find_element(By.CLASS_NAME, "gg-btn").click()
p.sleep(5)
chrome.find_element(By.XPATH, '//*[@id="content-header"]/div[2]/ul/li[2]/a/div').click()
p.sleep(5)
elementoTabela = chrome.find_element(By.XPATH, '//*[@id="content-container"]/div/table')

linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')

dflist = []

for linhaAtual in linhas:
    colunas = linhaAtual.find_elements(By.TAG_NAME, 'td')
    dados_linha = []
    for coluna in colunas:
        dados_linha.append(coluna.text)
    dflist.append(dados_linha)

df = pd.DataFrame(dflist)

arquivoExcel = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')
df.to_excel(arquivoExcel, sheet_name='Sheet1', index=False)
arquivoExcel.close()

p.sleep(5)
