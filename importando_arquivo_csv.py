

from pycep_correios import get_address_from_cep, WebService
import csv
with open('planilha-de-cep-pagina1.csv', encoding="utf8", errors='ignore') as arquivo:
    mostrar_arquivo = csv.reader(arquivo)
    next(mostrar_arquivo)    
    for cep in mostrar_arquivo:
        print(cep[0])  
        endereço_completo = get_address_from_cep(cep[0], webservice=WebService.CORREIOS)
        print(endereço_completo)
        
