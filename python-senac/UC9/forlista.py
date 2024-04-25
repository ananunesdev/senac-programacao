lista_notas  = [5, 6.5, 7, 2, 3.5, 5.9, 7.3, 2, 1, 0]
soma = 0

for nota in lista_notas:
    soma = soma + nota
    media = soma / len(lista_notas) #len é a quantidade de posições dentro de uma lista
print('Média: ', media)             #len significa contagem inteira dos elementos