#digitar senha
print('================================')
print('.::::: ACADEMIA PLAYSPORT :::::.')
print('================================')
print('     ...::: LOG IN :::...')
crefL = input('CREF do Instrutor: ')
senha = "54321"
leitura = " "
while(leitura != senha):
    leitura = input("Digite a senha: ")
    if leitura == senha: 
        print("Acesso liberado!")
    else: print("Senha incorreta! Tente novamente...")

print('================================')
print('   .::::: NOVA MATRÍCULA :::::.')
print('================================')
nome = input('Nome do cliente: ')
nasc = (input('Data de nascimento: [dd.mm.aa] '))

import random
matricula = random.randint(1000 , 9999)
print('Matrícula gerada:', matricula)
print()

peso = float(input('Peso: '))
altura = float(input('Altura: '))
cond_f = int(input('Biotipo Corporal: [1 - Ectomorfo | 2 - Mesomorfo | 3 - Endomorfo] '))
print()
if cond_f == 1:
    print(f'Biotipo corporal: \n'
        f' [x] Ectomorfo \n'
        f' [ ] Mesomorfo \n'
        f' [ ] Endomorfo \n')
elif cond_f == 2:
    print(f'Biotipo corporal: \n'
        f' [ ] Ectomorfo \n'
        f' [x] Mesomorfo \n'
        f' [ ] Endomorfo \n')
elif cond_f == 3:
    print(f'Biotipo corporal: \n'
        f' [ ] Ectomorfo \n'
        f' [ ] Mesomorfo \n'
        f' [x] Endomorfo \n')
else:
    print('')

meta = input('Meta do cliente: ')
print()
prof_aluno = input('Instrutor responsável: ')
crefA = input('CREF do instrutor: ')
print()
print('       ACADEMIA PLAYSPORT       ')
print('================================')
print('   .::::: FICHA DO ALUNO :::::.')
print('================================')
print('Nome: ',nome)
pr