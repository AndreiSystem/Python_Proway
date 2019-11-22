"""
nomes = ['Andrei', 'Gustavo', 'André']

nomes.sort()
print(nomes)
"""
"""
numeros = []

for n in range(1, 5):
    numeros.append(int(input('Digite um número: ')))


for i in range(5, 1, -1):
    
    if i % 2 == 1:
        
"""
lista = []

for n in range(1,10):
    lista.append(int(input('Digite um número: ')))

for i in range(len(lista), 0, -1):
    if lista[i-1] % 2 != 0:
        lista.remove(lista[i-1])
print(lista)