import pandas as pd
from selenium import webdriver

produtos = pd.read_excel(r'Produtos.xlsx')
produtos = produtos.fillna('-')
print(produtos)

driver = webdriver.Chrome()
driver.get('https://google.com')

input("Precione enter para finalizar")
