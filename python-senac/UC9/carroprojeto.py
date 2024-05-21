from datetime import date

data_atual = date.today()
data_atual = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

def infocarro():
    dono = input('Informe o nome do proprietário do carro: ')
    chassi = input('Informe o chassi do veículo: [8 últimos algarismos] ')
    placa = input('Informe a placa do veículo: ')
    modelo = input('Informe o modelo do carro: ')
    kmI = float(input("Insira a quilometragem inicial: "))
    kmF = float(input("Insira a quilometragem final: "))
    kmA = float(input("Insira a quilometragem atual: "))

    carro = {
        'Proprietário': dono,
        'Chassi': chassi,
        'Placa': placa,
        'Modelo': modelo,
        'Quilometragem inicial': kmI,
        'Quilometragem final': kmF,
        'Quilometragem atual': kmA
    }

    return carro

def abastecimento():
    print("---------------------------------------------")
    print("                  ABASTECIMENTO")
    print("---------------------------------------------")
    tipoc = 0
    while tipoc not in [1, 2, 3]:
        tipoc = int(input("Tipo de combustível: [ 1: Álcool | 2: Gasolina | 3: Diesel ] "))
        if tipoc == 1:
            print("O tipo de combustível é Álcool")
        elif tipoc == 2:
            print("O tipo de combustível é Gasolina")
        elif tipoc == 3:
            print("O tipo de combustível é Diesel")
        else:
            print("Opção inválida! Tente novamente.")

    preco = float(input("Valor do combustível: "))
    litrosA = float(input("Litros Abastecidos: "))
    valorA = preco * litrosA
    print(f'Valor do abastecimento: R$ {valorA:.2f}')
    return litrosA, valorA

def calcular_media(km_rodados, litrosA):
    print("---------------------------------------------")
    print("                     MÉDIA")
    print("---------------------------------------------")
    if litrosA != 0:
        mediaV = km_rodados / litrosA
        print(f"Média de KM por Litro: {mediaV:.2f}")
    else:
        mediaV = 0
        print("Não foi possível calcular a média, litros abastecidos é zero.")
    return mediaV

def resumo(carro, km_rodados, litrosA, valorA, mediaV):
    print("--------------------------------------------- ")
    print("                  RESUMO ")
    print("--------------------------------------------- ")
    print(f"Proprietário: {carro['Proprietário']}")
    print("--------------------------------------------- ")
    print(f"Placa: {carro['Placa']}")
    print(f"Chassi: {carro['Chassi']}")
    print(f"KM Inicial: {carro['Quilometragem inicial']}")
    print(f"KM Final: {carro['Quilometragem final']}")
    print(f"Total KM: {km_rodados}")
    print("--------------------------------------------- ")
    print(f"Tipo de combustível: {carro['Tipo de combustível']}")
    print(f"Valor do Abastecimento: R$ {valorA:.2f}")
    print(f"Média de KM por Litro: {mediaV:.2f}")
    print("---------------------------------------------")
    print("                   RESULTADO")
    print("---------------------------------------------")
    if mediaV > 10:
        print("Status: Acima da média")
    elif 9 <= mediaV <= 10:
        print("Status: Dentro da média")
    elif mediaV < 9:
        print("Status: Abaixo da média")
    else:
        print("Cálculo inválido")

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
        if km_rodados != 0:
            consumo = km_rodados / (carro['Quilometragem atual'] - carro['Quilometragem inicial'])
            print(f"Carro de {carro['Proprietário']}\n"
                  f" ({carro['Modelo']}):\n"
                  f" {consumo:.2f} km/l")
        else:
            print(f"Carro de {carro['Proprietário']} ({carro['Modelo']}): Não foi possível calcular o consumo devido à quilometragem rodado ser zero.")

def troca_pecas(km_rodados):
    print("---------------------------------------------")
    print("                TROCA DE PEÇAS")
    print("---------------------------------------------")
    if km_rodados < 5000:
        troca = "Parabéns! Seu veículo está em ótimo estado. Não há necessidade de trocar peças no momento."
    elif 5000 <= km_rodados <= 10000:
        troca = ("SUGESTÃO DE TROCA\n"
                 "========================\n"
                 "🔧 Óleo do Motor: Para garantir um desempenho suave e evitar desgastes.\n"
                 "🔧 Pneus: Verifique o estado e considere a substituição para segurança.\n")
    elif 10000 < km_rodados <= 15000:
        troca = ("SUGESTÃO DE TROCA\n"
                 "========================\n"
                 "🔧 Óleo do Motor: Troque o óleo para manter o motor funcionando perfeitamente.\n")
    elif 15000 < km_rodados <= 29999:
        troca = "Seu veículo está funcionando bem. Não há necessidade de troca de peças significativas neste momento."
    elif 30000 <= km_rodados <= 40000:
        troca = ("SUGESTÃO DE TROCA\n"
                 "========================\n"
                 "🔧 Cabo de Vela: Troque para garantir uma ignição eficiente e economia de combustível.\n")
    elif 40000 < km_rodados <= 50000:
        troca = ("SUGESTÃO DE TROCA\n"
                 "========================\n"
                 "🔧 Correia Dentada: Substitua para evitar danos graves ao motor.\n")

    print(troca)

def main():
    carros = []

    while True:
        print("======================")
        print('✤ GM CONSULT LTDA ✤')
        print("----------------------")
        print('Endereço: Rua Dois,270')
        print('CNPJ: 0.056.589.412-0001-58')
        print('Telefone: 31 3459 - 7515')
        print("----------------------")
        print()
        print("\nMenu - Data Atual: {}".format(data_atual))
        print("1. Inserir dados do veículo")
        print("2. Mostrar todos os veículos cadastrados")
        print("3. Calcular consumo")
        print("4. Troca de peças")
        print("9. Sair")
        print("======================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            carro = infocarro()
            carros.append(carro)
        elif opcao == "2":
            exibir_todos_carros(carros)
        elif opcao == "3":
            litrosA, valorA = abastecimento()
            for carro in carros:
                km_rodados = carro['Quilometragem final'] - carro['Quilometragem inicial']
                mediaV = calcular_media(km_rodados, litrosA)
                resumo(carro, km_rodados, litrosA, valorA, mediaV)
        elif opcao == "4":
            if carros:
                for carro in carros:
                    km_rodados = carro['Quilometragem final'] - carro['Quilometragem inicial']
                    troca_pecas(km_rodados)
            else:
                print("Não há veículos registrados.")
        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()