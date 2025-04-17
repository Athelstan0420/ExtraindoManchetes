
#Pegar as principais notícias/machetes 
#libre: beautifulsoup4(pip install) - melhor ferramenta
#Para receber essas informações e trata-las ele utiliza a libre: requests (pip install requests)

from bs4 import BeautifulSoup
import requests
import openpyxl 

def Extrair_informalções_site():
    try:
        workbook = openpyxl.load_workbook('/home/adriel/Documentos/Develop/ExtracaoMachetes/Sites_Classes.xlsx') #Para carregar a planilha;
        pagina_sites = workbook['Página1'] 
        for linha in pagina_sites.iter_rows(min_row=2):
            sites = linha[0].value 
            nomeClasses = linha[1].value
            #Requisicao:
            url = sites #Site que você quer extrair as informações.
            headers = {"User-Agent":"Mozilla/5.0"}#Simula um usuário acessando o navegador e não um programa.
            requisicao = requests.get(url, headers=headers)#Requisicao em si.
            code_pagina = BeautifulSoup(requisicao.text, "html.parser") #Pega o código fonte em html.  
            titulos_paginas = code_pagina.find_all(class_=f"{nomeClasses}")#Solicita a classe de títulos das materias
             # #Validação:
            if requisicao.status_code == 200: #Se o status da requisição dor igual a 200.
                for i in titulos_paginas:
                    print(i.text) #printar todos títulos já extraídos em forma de texto.
                    
        #200 = Requisição que deu certo.
        #301 = Redirecionado para outro site.
        #404 = Página não existe.      
    except:
        print("Erro!")

Extrair_informalções_site()

