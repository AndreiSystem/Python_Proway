



def coleta_str(mensagem= 'Digite um nome: '):
    while True:
        try:
            resp = str(input(mensagem))
        
        except:
            print('Apenas string!')

        else:
            return resp


metade1 = []
metade2 = []

for i in range(0,5):
    nome = coleta_str().title()
    metade1.append(nome)

for i in range(0,5):
    nome = coleta_str()
    metade2.append(nome)


metade2.reverse()

print(metade1 + metade2)







        