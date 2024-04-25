valorU = 0
while(valorU != 5):
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    
    print("1 : Adição | 2 : Subtração | 3 : Multiplicação | 4 : Divisão | 5 : Finalizar o programa")
    valorU = int(input("Escolha uma das opções: "))
    resultado = 0
    if(valorU == 1):
        resultado = n1 + n2
        print("A soma é ", resultado)
    elif (valorU == 2):
        resultado = n1 - n2
        print("A subtração é ", resultado)
    elif (valorU == 3):
        resultado = n1 * n2
        print("A multiplicação é ", resultado)
    elif (valorU == 4):
        resultado = n1 / n2
        print("A divisão é ", resultado)
    elif (valorU == 5):
        valorU = 5
        print("OK! Saindo...")
    else:
        print("Opção inválida! Tente novamente")
