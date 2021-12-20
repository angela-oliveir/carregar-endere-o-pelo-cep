from pycep_correios import get_address_from_cep, WebService
import csv
with open('planilha-de-cep-pagina1.csv', mode='r', encoding="utf8", errors='ignore') as arquivo:
    mostrar_arquivo = csv.reader(arquivo)
    next(mostrar_arquivo)    
    for cep in mostrar_arquivo:
        endereço_completo = get_address_from_cep(cep[0], webservice=WebService.CORREIOS)
        rua = endereço_completo['logradouro']
        bairro = endereço_completo['bairro']
        cidade = endereço_completo['cidade']
        cep = endereço_completo['cep']
        estado = endereço_completo['uf']
        print(f'Rua: {rua}')
        print(f'Bairro: {bairro}')
        print(f'Cidade: {cidade}')
        print(f'CEP{cep}')
        print(f'Estado: {estado}')
        print('\n')
