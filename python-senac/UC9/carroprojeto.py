from datetime import date

data_atual = date.today()
data_atual = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)

print(data_atual)

def infocarro():
    dono = input('Informe o nome do proprietário do carro: ')
    chassi = input('Informe o chassi do veículo: [8 últimos algarismos] ')
    placa = input('Informe a placa do veículo: ')
    modelo = input('Informe o modelo do carro: ')
    tipoc = input('Informe o tipo de combustível: ')
    kmI = float(input("Insira a quilometragem inicial: "))
    kmF = float(input("Insira a quilometragem final: "))
    kmA = float(input("Insira a quilometragem atual: "))

    carro = {
        'Proprietário' : dono,
        'Chassi' : chassi,
        'Placa' : placa,
        'Modelo' : modelo,
        'Quilometragem inicial' : kmI,
        'Quilometragem final' : kmF,
        'Quilometragem atual' : kmA,
        'Tipo de combustível' : tipoc,
    }

    return carro

def exibir_todos_carros(carros):
    if not carros:
        print('Não há veículos registrados.')
    else:
        for i, carro in enumerate(carros, start=1):
            print(f"Carro {i}:")
            for chave, valor in carro.items():
                print(f"{chave}: {valor}")
            print('')  

def calcular_consumo(carros):
    for carro in carros:
        km_rodados = carro['Quilometragem final'] - carro['Quilometragem inicial']
        consumo = km_rodados / (carro['Quilometragem atual'] / km_rodados)

        print(f'Carro de {carro['Proprietário']}\n
              f' ({carro['Modelo']}):\n 
              f' {consumo:.2f} km/l)

def main():
    carros = []
   
    while True:
        print ("\nMenu")
        print ("1. Inserir dados do veículo")
        print ("2. Mostrar todos os veículos cadastrados")
        print ('3. Calcular consumo')
        print ('4. Troca de peças')
        print ("9. Sair")
       
        opcao = input ("Escolha uma opção: ")
       
        if ( opcao == "1" ):
            carro = infocarro()
            carros.append(carro)
        elif (opcao == "2" ):
            if ( carros ):
                exibir_todos_carros(carros)
        elif ( carro == "3" ):
            calcular_consumo(carros)
        elif ( carro == "9" ):
            print ("Saindo...")
            break
        else:
            print ("Opção inválida")
if ( __name__ == "__main__"):
    main()



