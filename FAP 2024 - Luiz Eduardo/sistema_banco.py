import datetime

presente = datetime.datetime.now()
string_data_hoje = "{0}-{1}-{2}".format(presente.year, presente.month, presente.day)

contas = []

def buscar_conta(numero_buscado):
    for conta in contas:
        if conta.numero == numero_buscado:
            return conta
    return False

def deposito(numero_conta, valor):
    conta_encontrada = buscar_conta(numero_conta)
    if conta_encontrada:
        conta_encontrada.saldo += valor
    else:
        print('Conta não encontrada.')

def saque(numero_conta, valor):
    conta_encontrada = buscar_conta(numero_conta)
    if conta_encontrada:
        if conta_encontrada.saldo >= valor:
            conta_encontrada.saldo -= valor
        else:
            print('Operação negada. Saldo insuficiente. Saldo atual:', conta_encontrada.saldo)
    else:
        print('Conta não encontrada.')

class Conta:
    def __init__(self, nome_usuario, numero_conta, data_abertura):
        self.nome = nome_usuario
        self.numero = numero_conta
        self.data = data_abertura
        self.saldo = 0

print('Seja bem-vindo ao Banco FAP.')

while True:

    print('Que área você gostaria de acessar?')
    print('1. Área do cliente')
    print('2. Área do gerente')
    comando = int(input())
    if comando == 1:

        print('___________________________')
        print()
        print('O que deseja fazer? ')
        print('1. Criar conta')
        print('2. Fazer depósito')
        print('3. Fazer saque')
        print('4. Dados de conta')
        print('5. Sair')

        comando = int(input())
        if comando == 1:
            nome = input('Digite seu nome: ').title()
            numero = int(input('Digite um número único para sua conta: '))

            contas.append(Conta(nome, numero, string_data_hoje))

        if comando == 2:
            numero_conta = int(input('Número da conta: '))
            quantia = int(input('Quantia a ser depositada: '))
            deposito(numero_conta, quantia)
        
        if comando == 3:
            numero_conta = int(input('Número da conta: '))
            quantia = int(input('Quantia a ser sacada: '))
            saque(numero_conta, quantia) 

        if comando == 4:
            numero_conta = int(input('Número da conta: '))
            conta_encontrada = buscar_conta(numero_conta)
            if conta_encontrada:
                print('___________________________')
                print()
                print('DADOS DA CONTA: ')
                print('Nome:', conta_encontrada.nome)
                print('Número:', conta_encontrada.numero)
                print('Data de criação:', conta_encontrada.data)
                print('Saldo:', conta_encontrada.saldo)
            else:
                print('Conta não encontrada.') 

        if comando == 5:
            break
    if comando == 2:
        print('___________________________')
        print()
        print('O que deseja fazer? ')
        print('1. Edição de conta')
        print('2. Exclusão de conta')
        comando = int(input())
        if comando == 1:
            print('___________________________')
            numero_conta = int(input('Número da conta: '))
            conta_encontrada = buscar_conta(numero_conta)
            if conta_encontrada:
                novo_nome = input('Novo nome (deixe-o em branco para mantê-lo inalterado): ')
                novo_numero = input('Novo número (deixe-o em branco para mantê-lo inalterado): ')
                nova_data = input('Nova data (deixe-a em branco para mantê-la inalterada): ')
                novo_saldo = input('Novo saldo (deixe-o em branco para mantê-lo inalterado): ')

                conta_encontrada(novo_nome, novo_numero, nova_data, novo_saldo)