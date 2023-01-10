import os

import requests


def consulta():
    os.system('cls')
    print(80*'=')
    cep = input("[Digite um CEP para consultar na API da VIACEP]: ")

    requisition_api = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    avalia_status = requisition_api.status_code

    if avalia_status == 200:
        body = requisition_api.json()
        if body == {'erro': True}:
            print(80*'=')
            print(f'\n[O CEP fornecido: {cep}, é inexistente!]')
            print(80*'=')
            continuar_consulta()
        else:
            print(80*'=')
            print(requisition_api.content.decode('utf-8'))
            print(80*'=')
            salvar_consulta_em_arquivo(f'{requisition_api.text},\n')
            continuar_consulta()
    else:
        print(f'\n[CEP fornecido: {cep}, é inválido!]')
        continuar_consulta()


def salvar_consulta_em_arquivo(data):
    result = str(
        input("\n[Deseja salvar este resultado em arquivo local? (S = Sim)]: "))
    if result.upper() == "S":
        file_name = open('resultado.txt', 'a')
        file_name.writelines(data)
        file_name.close()
        print('\n[SALVO EM ARQUIVO !]')
    else:
        print('\n[NÃO SALVOU !]\n[Tecle "S" para Salvar!]')


def continuar_consulta():
    result = str(
        input("\n[Deseja realizar nova consulta? (S ou ENTER = Sim)]: "))
    consulta() if result.upper() == "S" or result == "" else os.system('cls')


if __name__ == '__main__':
    consulta()
