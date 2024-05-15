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

    paciente = {
        'Nome': nome,
        'Idade': idade,
        'Peso': peso,
        'Altura': altura,
        'IMC': imc
    }

def main():
    pacientes = []

    while True:
        print('\nMenu')
        print("1 - Cadastrar Cliente\n"
          "2 - Listar Clientes\n"
          "3 - Sair\n")
        
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            print('teste')
            paciente = registrar_paciente()
            pacientes.append(paciente)
        elif opcao == '2':
            print('teste 2')
        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente')
        
if __name__ == '__main__':
    main()