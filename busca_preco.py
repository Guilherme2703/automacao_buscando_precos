import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


produtos = pd.read_excel(r'Produtos.xlsx')
produtos = produtos.fillna('-')
print(produtos)

# Pegar preço amazon
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
except:
    print("Preço não encontrado.")

#Pegar preço da Lame
driver.get('https://www.americanas.com.br/smart-tv-4k-50-polegadas-lg-uhd-50ut8050-processador-a5-ger7-ai-alexa-chromecast-integrado-otimizador-de-jogos-webos-24-controle-smart-magic-7507042514/p?idsku=5725301&utm_source=YSMESP&utm_medium=buscappc&utm_campaign=alwayson-25&utm_content=bp_pl_sh_go_aloc_digital_apostassortimento_3p_aon25-00234&utm_term=pla_shopping&gad_source=1&gad_campaignid=22744334395&gbraid=0AAAAAD37Vpp_JV01DVyUO7oovGs82Yucz&gclid=Cj0KCQjw1JjDBhDjARIsABlM2SunsoJy03aCCv1IHpsRxNNoRQqvqLxcybiTTcbs3YwbiicYJS3uZWsaAmpdEALw_wcB')

try:
    preco_lame = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ProductPrice_productPrice__vpgdo'))
    ).text
    
    preco_lame = preco_lame.replace('R$', '').replace('.', '').replace(',', '.')
    preco_lame = float(preco_lame)
    print(preco_lame)
except:
    print("Preço não encontrado.")

#Pegar preço da mglu 
driver.get('https://www.magazineluiza.com.br/smart-tv-led-50-ultra-hd-4k-lg-50ut8050psa-thinq-ai-alexa-hdr10-3-hdmi-2-usb-wi-fi-bluetooth/p/af7kehg09h/et/tv4k/?seller_id=mega-mamute')

try:
    preco_mglu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'sc-dcJsrY eLxcFM sc-hgRRfv dfAhbD'))
    ).text
    
    preco_mglu = preco_mglu.replace('R$', '').replace('.', '').replace(',', '.')
    preco_mglu = float(preco_mglu)
    print(preco_mglu)
except:
    print("Preço não encontrado.")

input("Pressione enter para finalizar")
# sc-dcJsrY
