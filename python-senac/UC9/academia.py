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

print('===== TIPOS DE METAS =====')
print('1. Ganho de massa')
print('2. Perda de peso')
print('3. Aumento da capacidade física')
print('4. Esporte específico')
print('5. Recomendação médica')
print('6. N/A')
print()

meta = 'Inválido'

while meta == 'Inválido':
    meta = int(input("Insira o número correspondente à sua meta: "))
    if meta == 1:
        print('Meta: Ganho de massa')
    elif meta == 2:
        print('Meta: Perda de peso')
    elif meta == 3:
        print('Meta: Aumento da capacidade física')
    elif meta == 4:
        print('Meta: Esporte específico')
    elif meta == 5:
        print('Meta: Recomendação médica')
    elif meta == 6:
        print('')
    else:
        meta = 'Inválido'
        print('Operação inválida! Número inserido não corresponde com nenhuma das opções.')

print()
print('===============================')
prof_aluno = input('Instrutor responsável: ')
crefA = input('CREF do instrutor: ')

import os
os.system ('cls')

print()
print('       ACADEMIA PLAYSPORT       ')
print('================================')
print('   .::::: FICHA DO ALUNO :::::.')
print('================================')

from datetime import date

data_atual = date.today()
data_atual = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)

print('Início da matrícula:',data_atual)

print('Nome:',nome)
print('Data de nascimento:',nasc)
print('Matrícula:',matricula)
print('Instrutor:',prof_aluno)
print('CREF:',crefA)
print()


imc = peso / (altura * altura) 
print(f'IMC atual: {imc:.2f}')

#ficha de atividade sugerida e dieta

print('==============================================')
print(' .::::::: FICHA RECOMENDADA ::::::::.')

if meta == 1:
        print('Meta: Ganho de massa')
        print('==                 ==')
        print('. Levantamento de peso livre')
        print('. Exercícios compostos')
        print('. Exercícios de isolamento')
        print('. Acessórios')
        print('. Funcionais')
        print('. Treinamento Intervalado de Alta Intensidade (HIIT)')
        print()
        print('== NUTRIÇÃO ADEQUADA ==')
        print('Proteínas e calorias para crescimento muscular e balanço enérgetico positivo.')
        print('==                 ==')
elif meta == 2:
     print('Meta: Perda de peso')
     print('==                 ==')
     print('. Cardiovascular')
     print('. Resistência')
     print('. Atividades recreativas')
     print('. Aulas de grupo')
     print('. Treinos de Circuito')
     print('. Exercícios de baixo impacto')
     print()
     print('== NUTRIÇÃO ADEQUADA ==')
     print('Dieta equilibrada e saudável.')
     print('==                 ==')
elif meta == 3:
     print('Meta: Aumento da capacidade física')
     print('==                 ==')
     print('. Cardiovascular')
     print('. Treinamento de força')
     print('. Flexibilidade e mobilidade')
     print('. Coordenação e equilíbrio')
     print('. Resistência muscular localizada')
     print('. Potência')
     print()
     print('== NUTRIÇÃO ADEQUADA ==')
     print('Gorduras saudáveis, proteínas, carboidratos, alta hidratação.')
     print('==                 ==')
elif meta == 4:
     print('Meta: Esporte específico')
     print('==                 ==')
     print('Essa categoria deve ser adaptada de acordo com o objetivo de preparação.')
     print('==                 ==')
elif meta == 5:
     print('Meta: Recomendação médica')
     print('==                 ==')
     print('. Equilíbrio e estabilidade')
     print('. Flexibilidade')
     print('. Aeróbico')
     print('. Aulas de grupo e baixo impacto')
     print('==                 ==')
elif meta == 6:
     print('Essa categoria deve ser adaptada de acordo com o condicionamento físico e meta do aluno, caso seja diferente das outras alternativas. ')
     

