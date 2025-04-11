#importando pyautogui
#pyautogui é uma biblioteca que permite controlar o mouse e o teclado
import pyautogui

#vai ser usado para colcoar um outro tempo de espera em algum comando especifico
import time

#pandas permite trabalhar com planilhas
import pandas

#delay de meio segundo entre os comandos, para evitar que os comandos se "atropelem"
pyautogui.PAUSE = 0.5

#entrando no chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#pesquisando e entrando na url do site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)#esperando o site carregar

#campo de cadastro
pyautogui.click(x=688, y=374) #clicando no campo de login
pyautogui.write("lucastrindade.br64@gmail.com")#login exemplo
pyautogui.click(x=729, y=474)
pyautogui.write("123456")#senha exemplo
pyautogui.click(x=980, y=537)#logando no site

time.sleep(2)#esperando o site carregar

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:#para cada linha da minha tabela do arquivo .csv
    pyautogui.click(x=692, y=256)

    #adiconando um produto
    codigo = tabela.loc[linha, "codigo"]#pegando o codigo do produto da linha atual
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"]) # converte para string, sendo assim possivel adicionar os numeros no campo string = texto -> str()
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)#numero alto para garantir que role ate o comeco do site