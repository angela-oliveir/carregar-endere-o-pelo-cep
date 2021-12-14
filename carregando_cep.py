from pycep_correios import get_address_from_cep, WebService
opc = 'ns'
while True:
    cep = input('Digite seu cep: ')
    if len(cep) != 8:
        print('CEP inválido!')
        exit()        
        
    if len(cep) == 8:
        endereço_completo = get_address_from_cep(cep, webservice=WebService.APICEP)
        print(endereço_completo)

        opc = input('Deseja continuar? [S/N]: ').lower()

        while opc not in 'n' and opc not in 's':
            print('Opção inválida! ')
            opc = input('Deseja continuar? [S/N]: ').lower()

        if opc == 'n':
            print('Encerrando programa.')
            break




            
