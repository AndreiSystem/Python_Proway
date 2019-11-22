lista = []

for n in range(1,10):
    lista.append(int(input('Digite um número: ')))

for i in range(len(lista), 0, -1):
    if lista[i-1] % 2 != 0:
        lista.remove(lista[i-1])
print(lista)