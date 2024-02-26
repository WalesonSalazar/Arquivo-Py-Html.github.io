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
    time.sleep(4)
    
    pagina.fill('xpath=//*[@id="email"]', 'mauro.queiroz@saint-gobain.com')  #Login
    pagina.locator('xpath=//*[@id="btn-login"]').click()
    time.sleep(3)
    pagina.fill('xpath=//*[@id="password"]', '......')# Senha

    pagina.locator('xpath=//*[@id="btn-login"]').click()
    time.sleep(8)
   
    
#*******************************************************************************************
                  #Etapa de Envio de Relatório
#*******************************************************************************************
    #pagina.locator('xpath=//*[@id="navbarNav"]/ul/button[2]/span').click()#clicar em Módulos
    #time.sleep(2)
    #pagina.locator('xpath=//*[@id="dropdownModules_2"]').click()#clicar em Relatórios
    #time.sleep(2)
    #pagina.locator('xpath=//*[@id="dropdownModules_2_div"]/ul/li[1]/a').click()#Clicar em Planta
    #time.sleep(8)
    pagina.goto("https://mfm.wnology.io/page/reports")
    pagina.locator('xpath=//*[@id="select2-deviceTypeSelector-container"]').click()# clica tipo Campo TODOS
    time.sleep(2)
    pagina.fill('xpath=/html/body/span/span/span[1]/input', "Motor")#clica campo Tipo e Digita Motor
    time.sleep(2)
    pagina.keyboard.press("Enter")
    time.sleep(2)
    pagina.locator('xpath=//*[@id="logins-part"]/div[4]/div[4]/div[3]/div[1]/div/div/button').click() #clica Exibir

    pagina.locator('xpath=//*[@id="logins-part"]/div[4]/div[4]/div[3]/div[1]/div/div/div/a[4]').click()#clicar em 100
    time.sleep(2)
    pagina.locator('xpath=//*[@id="results"]/thead/tr/th[1]/div[1]/label/input').click()# cilca em None (para selecionar todos)
    time.sleep(2)
    pagina.locator('xpath=//*[@id="pills-profile-tab"]').click()# clica em Envio
    time.sleep(2)
    pagina.fill('xpath=//*[@id="information-part"]/div[1]/input', "Brasilit.Belém (Saint-Gobain)")# clica em Empresa e Digitar 
    time.sleep(2)
    pagina.locator('xpath=//*[@id="information-part"]/div[2]/input').click()#click para 
    pagina.locator('xpath=//*[@id="information-part"]/div[2]/input').click()#click para 
    pagina.locator('xpath=//*[@id="information-part"]/div[2]/input').click()#click para 
    #3 clicks ou Deletar email Atual

    pagina.fill('xpath=//*[@id="information-part"]/div[2]/input', ".waleson.tec@outlook.com")#Digitar Email destinatario Principal Apeana para teste

    pagina.fill('xpath=//*[@id="cc"]', ".waleson.salazar.tec@gamil.com")#.click clica campo cc e digita todos Email para receber Relatórios
    time.sleep(3)
    pagina.fill('xpath=//*[@id="information-part"]/div[5]/input' ,'Equipe IOT Brasilit-Belém') #clica campo Responsavel  e digitar equipe responsável
    time.sleep(2)
    pagina.fill('xpath=//*[@id="moreInfo"]' , 'Boa Tarde! Senhores. Segue envio do relatório.') #Clica em campo Outras Informações e Digitar informações Necessarios 
    time.sleep(2)
    pagina.locator('xpath=//*[@id="submitForm"]/span').click()#clicar em Gerar relatório
    time.sleep(16)
    #pagina.goto("https://mfm.wnology.io")#retorna pagina Inicial
    #time.sleep(10)
#*******************************************************************************************
                  #Etapa de baixar dados
#*******************************************************************************************
    #pagina.locator('xpath=//*[@id="oemMapComponentMap"]/div[1]/div[4]/div/div/div[1]').click()#Selecionar unidade no mapa
    #pagina.locator('xpath=//*[@id="mainPage"]/div[1]/div/ul/li[2]/a').click()#lista
    #time.sleep(5)
    #pagina.locator('xpath=//*[@id="oemMapComponentMap"]/div[1]/div[6]/div/div[1]/div/div/span[2]').click()#Ver Ativos
    pagina.goto("https://mfm.wnology.io/page/system/6040e01ef0e3e800060a6205")
    pagina.locator('xpath=//*[@id="select2-deviceTypeSelector-container"]').click()#clicar em todos Tipo
    time.sleep(5)
    pagina.fill('xpath=/html/body/span/span/span[1]/input', "Motor")#Motor
    time.sleep(1)
    pagina.keyboard.press("Enter")
    time.sleep(8)
    pagina.locator('xpath=//*[@id="tableContainer"]/div[2]/div[3]/div[1]/div/div/button/span[1]').click()#Clicar em exiber quantidades
    time.sleep(5)
    pagina.locator('xpath=//*[@id="tableContainer"]/div[2]/div[3]/div[1]/div/div/div/a[4]').click()#Clicar em 100 
    time.sleep(5)
    #pagina.on('download')
    # Aguarda o evento de download antes de clicar
    #downloadPromise = pagina.waitForEvent('download')
    #pagina.getByText('Download do arquivo').click()
    #download =downloadPromise

    pagina.locator('xpath=//*[@id="tableHeaderButtons"]/div[2]/button').click()#Clicar em baixar arquivo
    time.sleep(5)
    pagina.locator('xpath=//*[@id="tableHeaderButtons"]/div[2]/div/a[7]').click()#clicar Baixar em PDFs (MS-EXECEL)
    time.sleep(20)
    # Aguarda o término do processo de download e salva o arquivo baixado em algum lugar
    #download.saveAs('C:\Users\user\Desktop\Nova pasta' + download.suggestedFilename())
    time.sleep(5)
    #pagina.goto("https://mfm.wnology.io/")
    #time.sleep(5)
    #*********************************************************************************
           #Etapada de dar baixa nos estados criticos e Alertas
    #*********************************************************************************
    pagina.goto('https://mfm.wnology.io/page/events?isAll=true')
    #pagina.locator('xpath=//*[@id="mainPage"]/div[2]/div[2]/div[2]/a').click()#Ver Mais 
    time.sleep(5)
    #procura = "sim"
    while (True):
        pagina.locator('xpath=//*[@id="tableEventsDashboard"]/thead/tr/th[1]/div[1]/label/input').click()#Selecionar
        time.sleep(5)
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