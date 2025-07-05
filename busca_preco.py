import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


produtos = pd.read_excel(r'Produtos.xlsx')
produtos = produtos.fillna('-')
print(produtos)

# entrando no site da amazon
driver = webdriver.Edge()
driver.get('https://www.amazon.com.br/LG-50NANO80T-Processador-Chromecast-integrado/dp/B0D3JB8GYZ/ref=asc_df_B0D3JB8GYZ?mcid=769db38cdb513c40a442f4c7cc227410&tag=googleshopp00-20&linkCode=df0&hvadid=709964502896&hvpos=&hvnetw=g&hvrand=17184299404204777997&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1031811&hvtargid=pla-2323939420537&psc=1&language=pt_BR&gad_source=1')

# Quando o selenium começa a ler o site da amazom que
# um pop-up pedindo que clique em um botão contunuar
# isso faz com que a automação quebre, usando esse try 
# vamos meio que burlar esse pop-up e ter acesso a pagina

class_botao_acesso = 'a-button-text'
try:
    botao = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, class_botao_acesso))
    )
    botao.click()
    print("Botão clicado com sucesso!")
except:
    print("Não foi possível encontrar o botão.")

# Essas linhas de codigo irá copturar o preço do 
# produto que esta no site e colocar dentro de uma variavel

try:
    preco_amazon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'a-price-whole'))
    ).text
    
    preco_amazon = preco_amazon.replace('.', '')
    preco_amazon = float(preco_amazon)
    print(preco_amazon)
except:
    print("Preço não encontrado.")
    
input("Pressione enter para finalizar")
