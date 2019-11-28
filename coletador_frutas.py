def coletar_frutas():
    while True:
        f = str(input(f'Digite uma fruta: '))

        if f != 'laranja' and f != 'banana':
            return f
        else:
            print('Não é permitido essa fruta')


frutas = []

for i in range(0,5):
    frutinha = coletar_frutas()
    frutas.append(frutinha)

print(frutas)


"""
frutas = []

def coletar_frutas():
    i = 1
    while i <= 5:
        f = str(input(f'Digite a {i}° fruta: '))
        if f != 'laranja' and f != 'banana':
            frutas.append(f)
            i+= 1
        else:
            print('Não é permitido essa fruta')
       
coletar_frutas()
print(frutas)
"""