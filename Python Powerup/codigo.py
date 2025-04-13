import pyautogui
import time

# pyautogui.click -> clica em algum lugar
# pyautogui.press -> aperta 1 tecla
# pyautogui.write -> escreve um texto
# pyautogui.hotkey -> apertar uma combinação de teclas 

pyautogui.PAUSE = 0.5


# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o Chrome
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")

# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=750, y=403)
pyautogui.write("emailqualquer@gmail.com")
pyautogui.press("tab") 
pyautogui.write("123")

pyautogui.press("tab")
pyautogui.press("enter")
# Espera 3 segundos
time.sleep(3)


# Passo 3: Importar a base de dados
import pandas

tabela =  pandas.read_csv("produtos.csv ")

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=760, y=294)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    marca = tabela.loc[linha, "marca"]
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.press("tab")
    pyautogui.write(str(categoria))

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))

    custo = tabela.loc[linha, "custo"]
    pyautogui.press("tab")
    pyautogui.write(str(custo))

    obs = tabela.loc[linha, "obs"]
    pyautogui.press("tab")
    pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000000)

# Passo 5: Repetir para todos os produtos
