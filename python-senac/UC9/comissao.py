nome = str(input('Digite o nome do vendedor: '))
salario = float(input('Digite o salário: '))
vendas = float(input('Informe a quantidade de vendas do mês: '))
comissao = 0.15 * vendas
s_final = salario + comissao

import os
os.system ('cls')

print('==== RESUMO ====')
print('Nome: ', nome)
print('Salário final: (salário + comissão): ', s_final)
print('O salário do vendedor no mês é: R$ ', salario)
