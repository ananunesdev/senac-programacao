print('--------------------------------------')
print('==== ESCOLA ESTADUAL RAIMUNDINHA ====')
print('--------------------------------------')

qtd = int(input('Insira a quantidade de alunos: '))
contador = 0
aprovado = 0
reprovado = 0
recuperacao = 0
while (contador < qtd):
    contador = contador + 1
    nome = input('Insira o nome do aluno: ')

    nota1 = float(input('Insira a 1° nota: '))
    nota2 = float(input('Insira a 2° nota: '))
    nota3 = float(input('Insira a 3° nota: '))
    nota4 = float(input('Insira a 4° nota: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
        aprovado = aprovado + 1
        print('O aluno(a)' , nome , 'foi aprovado com nota ', media, '.')
    elif media < 4.5:
        reprovado = reprovado + 1
        print('O aluno(a)' , nome , 'foi reprovado com nota ', media, '.')
    else:
        recuperacao = recuperacao + 1 
        print('O aluno(a)' , nome , 'está de recuperação.')

print('A quantidade de alunos aprovados é de ', aprovado)
print('A quantidade de alunos reprovados é de ', reprovado)
print('A quantidade de alunos de recuperação é de ', recuperacao)
