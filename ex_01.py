#Digite 3 números e diga qual o maior.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
"""
 n1 = 2
 n2 = 3
 n3 = 4
"""


if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n3:
    print(n2)
else:
    print(n3)


"""
if n1 < n2 > n3:
    print(n2)
elif n2 < n3 > n1:
    print(n3)
else:
    print(n1)
"""

