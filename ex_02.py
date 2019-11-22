#Digite 10 valores e mostre o maior
maior = -99999999
i = 1
while i < 10:

    n = int(input('Digite um número: '))
    if n > maior:
        maior = n

    i+=1

print(f'O valor maior digitado é {maior}')
