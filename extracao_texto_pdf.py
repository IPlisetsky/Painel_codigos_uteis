import os
import pdfplumber


pasta_arquivos = r"DIRETORIO"
lista_arquivos = os.listdir(pasta_arquivos)
for arquivo in lista_arquivos:
    try:
        if ".pdf" in arquivo:
            print(arquivo)
            pdf= pdfplumber.open(f'{pasta_arquivos}/{arquivo}')
            page = pdf.pages[0]
            text = page.extract_text()
            
            linhas = text.split('\n')
            for i, linha in enumerate(linhas):
                if "CÓDIGO" in linha:
                    print(f"ENCONTRADO NA LINHA {i}")
                    colunas = text.split('\n')[i].split(' ')
                    valores = text.split('\n')[i+1].split(' ')
                    print(valores)
                else:
                    pass            
        else:
            pass
    except Exception as e:
        print(f"ERRO: {e}")