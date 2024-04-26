NotaBimestral = [20, 15.5, 15, 10]
soma = 0

for nota in NotaBimestral:
    soma = soma + nota
print('Nota: ', soma)
if soma >= 70:
    print('Situação: Aprovado! Pois a nota do aluno é ', soma, "%")
elif soma <= 49:
    print('Situação: Reprovado! Pois a nota do aluno é ', soma, "%")
else:
    print('Situação: Recuperação! Pois a nota do aluno é ', soma, "%")