def idade_valida(idade):
    return idade >= 18

def listagem():
    arquivo = open('pessoas.txt', 'r')
    conteudo = arquivo.readlines()
    
    for pessoa in conteudo:
        dados = pessoa.split(',')
        print(f'nome = {dados[0]} idade = {dados[1]}')

 

def cadastro():
    def registrar():
        arquivo = open('pessoas.txt', 'r')
        conteudo = arquivo.readlines()
        
        conteudo.append(f'{nome},{idade}\n')

        arquivo = open('pessoas.txt', 'w')
        arquivo.writelines(conteudo)

        arquivo.close()

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    
    if idade_valida(idade):
        print('Cadastro com sucesso: ', nome)
        print(f'Idade válida: {idade} anos')

        registrar()

    else:
        print(f'A idade de {nome} é inválida para o cadastro.')
    




def opcoes():
    
    return int(input('Digite uma das opções:\n'
        '2. Listagem\n'
        '1. Cadastro\n'
        '0. Sair\n'
    ))
    print('opção: ', opcao)



def main():
    opcao = opcoes() 
 
    if opcao == 1:
        cadastro()  
    
    elif opcao == 2:
        listagem()

    elif opcao != 0:
        print("Opção nao encontrada.")
    
    if opcao != 0:
        main()
    else: 
        print('saindo...')

main()
print('[SAIU] Volte sempre!')




