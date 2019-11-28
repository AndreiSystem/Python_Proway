categoria = ('comedia', 'ação', 'aventura', 'romance', 'suspense', 'terror')

restricoes = ('gore', 'comédia romântica', 'comédia dramática', 'musical')


while True:
    f = (input('Digite um filme: ').lower().strip())
    if f in categoria and f not in restricoes:
        print(f'Filme de categoria disponivel: {f}. Bom filme!')
        break
    else:
        print('Essa categoria não está disponivel!')
        
        