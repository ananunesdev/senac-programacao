from datetime import date

data_atual = date.today()
data_atual = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)

print(data_atual)

print("--------------------------------------------- ")
print("                  MOTORISTA ")
print("--------------------------------------------- ")

matricula = int(input("Matrícula: "))
motorista = (input("Motorista: "))

print("--------------------------------------------- ")
print("                    VEÍCULO ")
print("--------------------------------------------- ")

placa = (input("Placa: "))
numeroV = int(input("N° do Veículo: "))
kmI = int(input("KM Inicial: "))
kmF = int(input("KM Final: "))

totalKM = kmF - kmI

print("Total KM: ", totalKM)

print("---------------------------------------------")
print("                  ABASTECIMENTO")
print("---------------------------------------------")
tipoA = 0
tipoA = int(input("Tipo de combustível: [ 1:  Álcool | 2 : Gasolina | 3 : Diesel ] "))
if (tipoA == 1):
    print("O tipo de combustível é Álcool")
elif(tipoA == 2):
    print("O tipo de combustível é Gasolina")
elif(tipoA == 3):
    print("O tipo de combustível é Diesel")
else:
    print("Opção inválida! Tente novamente.")

preco = float(input("Valor do combustível: "))
litrosA = float(input("Litros Abastecidos: "))
valorA = preco * litrosA
print(f'Valor do abastecimento: , {valorA:.2f}')

print("---------------------------------------------")
print("                     MÉDIA")
print("---------------------------------------------")

mediaV = totalKM / litrosA 
print("Média de KM por Litro: ", mediaV)

import os 
os. system('cls')

print("--------------------------------------------- ")
print("                  RESUMO ")
print("--------------------------------------------- ")
print("Matrícula: ",matricula)
print("Motorista: ",motorista)
print("--------------------------------------------- ")
print("Placa: ",placa)
print("N° do Veículo: ",numeroV)
print("KM Inicial: ",kmI)
print("KM Final: ",kmF)
print("Total KM: ", totalKM)
print("--------------------------------------------- ")
print("Tipo de combustível: ", tipoA)
print("Valor do Abastecimento: ", valorA)
print("Média de KM por Litro: ", mediaV)

print("---------------------------------------------")
print("                   RESULTADO")
print("---------------------------------------------")

if (mediaV > 10 ):
    print("Status: Acima da média")
elif (mediaV >= 9) and (mediaV <= 10):
    print("Status: Dentro da média")
elif (mediaV < 9):
    ("Status: Abaixo da média")
else:
    print("Cálculo inválido")
