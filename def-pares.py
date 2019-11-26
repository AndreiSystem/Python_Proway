
def recolhe_num():
    i = 1

    while i <= 10:
        pares.append(int(input('Digite um valor: ')))

        i+=1


def procura_pares():
    
    pares_lista = []
    if pares % 2 == 0:
        pares_lista.append(pares)

    return pares_lista


recolhe_num()