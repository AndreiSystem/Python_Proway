modelos = ['fusca', 'gol', 'vectra', 'corola', 's10']

km_por_l = [6, 15, 14, 18, 12]

economico = max(km_por_l)
for i in range(0, len(modelos)):
    if km_por_l[i] == economico:
        print(f'Modelo mais economico {modelos[i]}')
        
for i in range(len(modelos)):
    print(f'{modelos[i]} faz {100 / km_por_l[i]:.1f}L em 1000km')




