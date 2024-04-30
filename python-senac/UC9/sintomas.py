dc = 0
febre = 0
da = 0
mv = 0
do = 0
tosse = 0
fa = 0
dg = 0
abdominal = 0
diarreia = 0
fadiga = 0

nome = input('Digite seu nome completo ')
cpf = input('Digite o número do seu CPF ')
 
while True:
    dc = int(input("Você está com Dor de cabeça? [0 - Não | 1- Sim]: "))
    if (dc == 1) or (dc == 0):
        break
    else:
        print("Por favor responda com 0 ou 1!")
while True:
    febre = int(input("Você está com Febre [0 - Não | 1- Sim]: "))
    if (febre == 1) or (febre == 0):
        break
    else:
         print("Por favor, responda com 0 ou 1!")
while True:
    da = int(input("Você está com Dor nas articulações? [0 - Não | 1- Sim]: "))
    if (da == 1) or (da == 0):
        break
    else:
        print("Por favor, responda com 0 ou 1!")
while True:
    mv = int(input("Você está com Manchas vermelhas na pele? [0 - Não | 1- Sim]: "))
    if (mv == 1) or (mv == 0):
        break
    else:
        print("Por favor, responda com 0 ou 1!")
while True:
    do = int(input("Você está com Dor atrás dos olhos? [0 - Não | 1- Sim]: "))
    if (do == 1) or (do == 0):
        break
    else:
        print("Por favor, responda com 0 ou 1!")
while True:
    tosse = int(input("Você está Tossindo? [0 - Não | 1- Sim]: "))
    if (tosse == 1) or (tosse == 0):
        break
    else:
        print("Por favor, responda com 0 ou 1!")
while True:
    fa = int(input("Você está com Falta de ar? [0 - Não | 1- Sim]: "))
    if (fa == 1) or (fa == 0):
        break
    else:
        print("Por favor, responda com 0 ou 1!")
while True:
    dg = int(input("Você está com Dor de garganta? [0 - Não | 1- Sim]: "))
    if (dg == 1) or (dg == 0):
        break
    else:
        print("Por favor, responda com 0 ou 1!")
while True:
    abdominal = int(input("Você está com Dor abdominal? [0 - Não | 1- Sim]: "))
    if (abdominal == 1) or (abdominal == 0):
        break
    else:
        print("Por favor, responda com 0 ou 1!")
while True:
    diarreia = int(input("Você está com Diarreia? [0 - Não | 1- Sim]: "))
    if (diarreia == 1) or (diarreia == 0):
        break
    else:
        print("Por favor, responda com 0 ou 1!")
while True:
    fadiga = int(input("Você está com Fadiga? [0 - Não | 1- Sim]: "))
    if (fadiga == 1) or (fadiga == 0):
        break
    else:
        print("Por favor, responda com 0 ou 1!")
       
 
if (dc == 1) and (febre == 1) and (tosse == 1) and (fadiga == 1):
    doenca = "Gripe"
    print(doenca)
elif (dc == 1) and (do == 1) and (febre == 1) and (da == 1) and (mv == 1):
    doenca = "Dengue"
    print(doenca)
elif (tosse == 1) and (fa == 1) and (febre == 1) and (dg == 1) and (abdominal == 1):
    doenca = "Covid 19"
    print(doenca)
else:
    print('Não foi possível chegar em um diagnóstico.')

crm = int(input('Digite o CRM do médico'))

while medico == 'Invalido':
    if (crm == 123456):
        medico = 'Dr. Matheus Pereira'
    elif (doenca == 654321):
        medico = 'Dr. Mateus Vital'
    else:
        medico = 'Invalido'
        print('Médico inválido, favor abrir chamado para cadastrar.')

while cadastrocid == "Invalido":
    if (doenca == "Gripe"):
        cid = "J11"
    elif (doenca == "Dengue"):
        cid = "A90"
    elif (doenca == "Covid"):
        cid = "B34"
    else:
        cadastrocid = "Invalido"
        print("CID inválido, favor digitar novamente.")


import os
os.system ('cls')
   
print("-------------------------------")
print("     DIAGNÓSTICO")
print("-------------------------------")

print('Nome completo: ', nome)
print('CPF: ', cpf)
print('')
print('--------',doenca,'----------')
