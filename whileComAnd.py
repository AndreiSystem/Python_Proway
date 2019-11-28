
item = []
resp = ''

print('Digite 5 itens para registrar ou aperte SAIR')
while resp != 'sair' and len(item) < 5:
    resp = (input('Digite um item: ').lower().strip())
    if resp != 'sair':
        item.append(resp)


print(item)