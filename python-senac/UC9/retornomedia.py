print('--------------------------------------')
print('==== ESCOLA ESTADUAL RAIMUNDINHA ====')
print('--------------------------------------')

qtd = int(input('Insira a quantidade de alunos: '))
contador = 0
while (contador < qtd):
    contador = contador + 1
    nome = input('Insira o nome do aluno: ')

    nota1 = float(input('Insira a 1° nota: '))
    nota2 = float(input('Insira a 2° nota: '))
    nota3 = float(input('Insira a 3° nota: '))
    nota4 = float(input('Insira a 4° nota: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
        print('O aluno' , nome , 'foi aprovado com nota ', media, '.')
    elif media < 4.5:
        print('O aluno' , nome , 'foi reprovado com nota ', media, '.')
    else:
        print('O aluno' , nome , 'está de recuperação.')