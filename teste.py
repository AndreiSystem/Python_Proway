
numeros = []
for i in range(0,3):
    n = int(input('Digite um valor: '))

    numeros.append(n)

print(f'O menor valor da lista é {min(numeros)}')
print(f'O maior valor da lista é {min(numeros)}')
print(f'A média da lista {numeros} é de: {sum(numeros) / 3:.2f}')