#Digite o menor valor
menor = 2**64
i = 0

while i < 10:
    n = int(input('Digite um número: '))
    if n < menor:
        menor = n

    i+=1

print(f'O menor número é {menor}') 