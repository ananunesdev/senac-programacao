def main():
    pacientes = []

    while True:
        print('\nMenu')
        print("1 - Cadastrar Cliente\n"
          "2 - Listar Clientes\n"
          "3 - Listar Personal Trainer\n"
          "4 - Sair\n")
        
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