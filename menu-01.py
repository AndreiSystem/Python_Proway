def idade_valida(idade):
    return idade >= 18

def cadastro():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    
    if idade_valida(idade):
        print('Cadastro com sucesso: ', nome)
        print(f'Idade válida: {idade} anos')
    else:
        print('Idade inválida!')
    


opcao = 0

def opcoes():
    return int(input('Digite uma das opções?\n'
        '1. Cadastro\n'
        '0. Sair\n'
    ))
    print('opção: ', opcao)

opcao = opcoes()

while opcao != 0: 
    if opcao == 1:
        cadastro()     
    else:
        print("Opção nao encontrada.")
    opcao = opcoes()


print('Volte sempre!')