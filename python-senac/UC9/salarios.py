print()

print('------------------------------------------')
print('.::::::          DADOS        :::::.')
print('------------------------------------------')
print('      Informe seus dados abaixo')
nome = input('Nome: ')
cpf = int(input("CPF: "))
funcaof = input('Função: ')
cbo = int(input('CBO: '))
print('------------------------------------------')
salario = float(input('Salário: '))
conf_vt = int(input('Você recebe vale transporte? 0 - Não | 1 - Sim '))
filho = int(input('Você possui quantos filhos? '))
print()
perce = 0
aum = 0
novo_s = 0

inss = 0
irrf = 0


if salario <= 1420.00:
    perce = '20%'
    aum = (salario / 100) * 20
    novo_s = salario + aum
elif salario > 1420.00 and salario <= 2590.00:
    perce = '15%'
    aum = (salario / 100) * 15
    novo_s = salario + aum
elif salario > 2590.00 and salario <= 4326.00:
    perce = '10%'
    aum = (salario / 100) * 10
    novo_s = salario + aum
else:
    perce = '5%'
    aum = (salario / 100) * 5
    novo_s = salario + aum

if conf_vt == 1:
    vt = salario * 0.06
elif conf_vt == 0:
      conf_vt = 0

if salario >= 2259.21 and salario <= 2828.65:
     irrf = (salario / 100) * 7.5
elif salario >= 2828.66 and salario <= 3751.05:
     irrf = (salario / 100) * 15
elif salario >= 3751.06 and salario <= 4664.68:
      irrf = (salario / 100) * 22.5
elif salario > 4664.69:
      irrf = (salario / 100) * 27.5
else:
      irrf = 0

if salario <= 1655.98:
      familia = filho * 62.00
elif salario <= 1655.99 and salario >= 1754.18:
      familia = filho * 59.82
elif salario <= 1754.19 and salario >= 1819.26:
      familia = filho * 62.04
else:
      filho = 0


# \n quebra linha

print('------------------------------------------')
print('     .::::     HOLERITE        ::::.')
print('------------------------------------------')

print('Nome: ', nome)
print('CPF: ', cpf)
print('Função: ', funcaof)
print('CBO', cbo)

print()
print('REAJUSTE')
print(f'Salário antes do reajuste: R$ {salario:.2f}\n'
      f'Percentual de aumento {perce}\n'
      f'Valor do aumento salarial: R$ {aum:.2f}\n'
      f'Salário após o reajuste: R$ {novo_s:.2f}\n')

print()
print('DESCONTOS')
print(f'Desconto Vale-Transporte: {vt:.2f}\n'
      f'Desconto do Imposto de Renda {irrf:.2f}\n'
      f'Salário-família: {familia:.2f}')

print()
print('INSS')
if (salario <= 1302):
        scal = (salario / 100) * 7.5
        print(f'Sua contribuição é de {scal:.2f}')
        print("Sua alíquota é de 7.5%.")
elif (salario >= 1302.1) and (salario <= 2371.29):
        scal = (salario / 100) * 9
        print('Sua contribuição é de', scal)
        print("Sua alíquota é de 9%.")
elif (salario >= 2371.30) and (salario <= 3856.94):
        scal = (salario / 100) * 12
        print('Sua contribuição é de', scal)
        print("Sua alíquota é de 12%.")
elif (salario >= 3856.95) and (salario <= 7507.49):
        scal = (salario / 100) * 14
        print('Sua contribuição é de', scal)
        print("Sua alíquota é de 14%.")