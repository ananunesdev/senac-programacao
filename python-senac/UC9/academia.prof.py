def exibir_ficha(paciente):
    print('\nFicha de Paciente')
    print('===================')
    for chave, valor in paciente.items():
        if chave == 'IMC' and valor is not None:
            print(f'{chave}: {valor:.2f}')
        else:
            print(f'{chave}: {valor}')

def avaliacao_imc (imc):
    if imc is None:
        return 'Altura e/ou peso inválidos. Não é possível calcular o IMC.'
    elif imc < 18.5:
        return 'Abaixo do peso. É recomendável uma dieta equilibrada e acompanhamento nutricional.'
    elif 18.5 <= imc < 24.9:
        return 'Peso normal. Continue com uma alimentação saudável e uma dieta balanceada.'
    elif 25 <= imc < 29.9:
        return 'Sobrepeso. Sugere-se um plano de exercício e alterações na alimentação.'
    elif 30 <= imc < 34.9:
        return 'Obesidade Grau I.'
    elif 35 <= imc < 39.9:
        return 'Obesidade Grau II.'
    else:
        return 'Obesidade Grau III.'
    
    #elif (imc >= 18.5) and (imc < 24.9):

def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return imc
    except ZeroDivisionError:
        return None

def registrar_paciente():
    nome = input('Digite o nome do paciente: ')
    idade = int(input('Digite a idade do paciente: '))
    peso = float(input('Digite o peso do paciente (em Kg): '))
    altura = float(input('Digite a altura do paciente (em metros): '))

    imc = calcular_imc(peso, altura)

    avaliacao = avaliacao_imc(imc)

    paciente = {
        'Nome': nome,
        'Idade': idade,
        'Peso': peso,
        'Altura': altura,
        'IMC': imc,
        'Avaliacao': avaliacao
    }

    return paciente

def main():
    pacientes = []

    while True:
        print('\nMenu')
        print("1 - Cadastrar Cliente\n"
          "2 - Listar Clientes\n"
          "3 - Sair\n")
        
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            paciente = registrar_paciente()
            pacientes.append(paciente)
        elif opcao == '2':
            if pacientes:
                exibir_ficha(pacientes[-1])
            else:
                print('Nenhum paciente registrado.')
        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente')
        
if __name__ == '__main__':
    main()