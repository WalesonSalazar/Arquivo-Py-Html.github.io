from playwright.sync_api import sync_playwright 

import time
import pyautogui
#https://www.bing.com/videos/riverview/relatedvideo?q=nvegador+est%c3%a1+bloqueando+dowload&mid=6F353C19472198F911326F353C19472198F91132&FORM=VIRE
#********************************************************************************
                #Etapa de acessar o site elogar na conta 
#********************************************************************************
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)

    pagina = navegador.new_page()
 
    pagina.goto("https://mfm.wnology.io/login")
    time.sleep(5)
    
    pagina.fill('xpath=//*[@id="email"]', 'mauro.queiroz@saint-gobain.com')  #Login
    pagina.locator('xpath=//*[@id="btn-login"]').click()
    time.sleep(3)
    pagina.fill('xpath=//*[@id="password"]', 'Motor@weg')# Senha

    pagina.locator('xpath=//*[@id="btn-login"]').click()
    time.sleep(8)
    #pagina.locator(".header").screenshot('path=//*[@id="mainPageOverview"]/div')#visão Geral
    #pagina.get_by_role('xpath=//*[@id="mainPageOverview"]/div/div[2]').screenshot()
    #time.sleep(3)
#*******************************************************************************************
                  #Etapa de baixar dados
#*******************************************************************************************
    pagina.locator('xpath=//*[@id="oemMapComponentMap"]/div[1]/div[4]/div/div/div[1]').click()#Selecionar unidade no mapa
    #pagina.locator('xpath=//*[@id="mainPage"]/div[1]/div/ul/li[2]/a').click()#lista
    time.sleep(5)
    pagina.locator('xpath=//*[@id="oemMapComponentMap"]/div[1]/div[6]/div/div[1]/div/div/span[2]').click()#Ver Ativos
    #pyautogui.move(-600, 300)

    #procurar = "sim"

    #while procurar == "sim":
        #try:
            #imge = pyautogui.locateCenterOnScreen("VerAtivos.PNG")
           #pyautogui.click(imge.x, imge.y)       
        
            #procurar = "não"
        #except:
            #time.sleep(1)
    
            #print("aguarda2")
            
    #time.sleep(8)
    pagina.locator('xpath=//*[@id="select2-deviceTypeSelector-container"]').click()#clicar em todos Tipo
    #pagina.locator('xpath=//*[@id="select2-plants-container"]').click()#Planta ou Grupo
    #time.sleep(5)
    #pagina.locator('xpath=//*[@id="select2-plants-result-f7sj-6040e01ef0e3e800060a6205"]').click()#Brasilit
    #pyautogui.press('enter')
    #pagina.locator('xpath=//*[@id="select2-deviceTypeSelector-container"]').click()#Tipo2
    time.sleep(5)

    pagina.fill('xpath=/html/body/span/span/span[1]/input', "Motor")#Motor
    time.sleep(1)
    pagina.keyboard.press('Enter')
    time.sleep(8)
    
    #pagina.locator('xpath=//*[@id="select2-deviceTypeSelector-result-h1bl-group_motor"]').click()#Motor2
    #pyautogui.press("enter")
    
    #pagina.locator('xpath=//*[@id="select2-deviceTypeSelector-result-9vsb-group_motor"]').click()#clicar em motor
    #time.sleep(5)
    #clicar e saúde
    #clicar em todos
    pagina.locator('xpath=//*[@id="tableContainer"]/div[2]/div[3]/div[1]/div/div/button/span[1]').click()#Clicar em exiber quantidades
    time.sleep(5)
    pagina.locator('xpath=//*[@id="tableContainer"]/div[2]/div[3]/div[1]/div/div/div/a[4]').click()#Clicar em 100 
    time.sleep(5)
    pagina.locator('xpath=//*[@id="tableHeaderButtons"]/div[2]/button').click()#Clicar em baixar arquivo
    time.sleep(5)
    pagina.locator('xpath=//*[@id="tableHeaderButtons"]/div[2]/div/a[7]').click()#clicar Baixar em PDFs (MS-EXECEL)
    time.sleep(8)
    pagina.goto("https://mfm.wnology.io/")
    time.sleep(10)
    #*********************************************************************************
           #Etapada de dar baixa nos estados criticos e Alertas
    #*********************************************************************************

    pagina.locator('xpath=//*[@id="mainPage"]/div[2]/div[2]/div[2]/a').click()#Ver Mais 
    time.sleep(5)
    pagina.locator('xpath=//*[@id="tableEventsDashboard"]/thead/tr/th[1]/div[1]/label/input').click()#Selecionar
    time.sleep(2)
    pagina.locator('xpath=//*[@id="resolveEvents"]').click()#Resolver
    time.sleep(2)
    pagina.locator('xpath=//*[@id="tableEventsDashboard"]/thead/tr/th[1]/div[1]/label/input').click()#Selecionar
    time.sleep(2)
    pagina.locator('xpath=//*[@id="resolveEvents"]').click()#Resolver
    time.sleep(8)
    pagina.locator('xpath=//*[@id="tableEventsDashboard"]/thead/tr/th[1]/div[1]/label/input').click()#Selecionar
    time.sleep(2)
    pagina.locator('xpath=//*[@id="resolveEvents"]').click()#Resolver
    time.sleep(5)    

   # //*[@id="mainContent"]/div[10]/div[2]/div/div[1]/div[1]

#//*[@id="tableEventsDashboard"]/thead/tr/th[1]/div[1]/label/input

#//*[@id="tableEventsDashboard"]/thead/tr/th[1]/div[1]/label/input

#//* [@id="resolveEvents"]