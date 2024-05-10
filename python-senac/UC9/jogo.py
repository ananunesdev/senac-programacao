ganhou = 0
tentativas = 0
chute = 0

import random
numerosecreto = int(random.randint(1 , 10))

while (chute != numerosecreto):
    tentativas = tentativas + 1
    chute = int(input('Qual é o seu chute? '))

    if (chute < 0):
        print('Você não pode chutar números negativos.')

    elif (chute == numerosecreto):
        print('Parabéns, você acertou!')
        print('Seu chute foi ',chute,'!', 'Você tentou ',tentativas,'vezes')

    elif (chute > numerosecreto):
        print('Seu chute foi maior que o número secreto!')
    else:
        print('Seu chute foi menor que o número secreto!')