


import csv

with open('planilha-de-cep-pagina1.csv', encoding="utf8", errors='ignore') as arquivo:
    mostrar_arquivo = csv.reader(arquivo)
    next(mostrar_arquivo)
    for arquivo_csv in mostrar_arquivo:
        print(arquivo_csv)