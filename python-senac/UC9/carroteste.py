def rgcarro():
    #Solicitação dos dados do carro
    dono = input("Digite o nome do proprietário do carro: ")
    modelo = input("Insira o modelo do carro: ")
    kmi = float(input("Insira a quilometragem inicial: "))
    kmf = float(input("Insira a quilometragem final: "))
    kma = float(input("Insira a quilometragem atual: "))
 
    carro = {
        'Proprietario': dono,
        'Modelo': modelo,
        ''
   
   
 
 
    }
 
 
def main():
    carros = []
 
    while True
        print("\nMenu")
        print("1. Inserir dados do veículo")
        print("2. Mostrar ddos do último veículo registrado")
        print("3. Mostrar todos os veículos cadastrados")
        print("9. Sair")
 
        opcao = input("Escolha uma opção")
       
        if(opcao == "1"):
            carro = rgcarro()
            carros.append(carro)
        elif (opcao == "2"):
            if (carro):
                exibirfc(carros[-1])
            else:
                print("Nenhum carro registrado")
        elif (carro == "3"):
            exibirtc(carros_)
        elif (carro == 9):
            print("Saindo...")
        else:
            print("Opção inválida")
 
if (__name__ == "__mani__"):
    main()

def pecas1( kma ):
    if (kma == None):
        return ( "Quilometragem atual inválida")
    elif (kma >= 20000):
        velas = ( "Velas: necessário troca")
        correia = ( "Correia dentada: não precisa ser trocada ainda")
        pneu = ( "Pneus: não precisa ser trocado ainda")
        return f"{velas}\n{correia}\n{pneu}\n"
    elif (kma >= 50000):
        velas = ( "Velas: necessário troca")
        correia = ( "Correia dentada: necessário troca")
        pneu = ( "Pneus: não precisa ser trocado ainda")
        return f"{velas}\n{correia}\n{pneu}\n"
    elif (kma >= 60000):
        velas = ( "Velas: necessário troca")
        correia = ( "Correia dentada: necessário troca")
        pneu = ( "Pneus: necessário troca")
        return f"{velas}\n{correia}\n{pneu}\n"
 
def rgcarro ():
    #Solitação dos dados do carro
    dono = input ("Digite o nome do proprietário do carro: ")
    modelo = input ("Insira o modelo do carro: ")
    tipoc = input ( "Insira o tipo do combustível: ")
    kmi = float ( input ("Insira a quilometragem inicial: "))
    kmf = float ( input ("Insira a quilometragem final: "))
    kma = float ( input ("Insira a quilometragem atual: "))
   
    p1 = pecas1 ( kma)
    p2 = pecas2 (kmf,kmi)
   
    carro = {
        'Proprietário' : dono,
        'Modelo' : modelo,
        'Quilometragem inicial' : kmi,
        'Quilometragem final' : kmf,
        'Quilometragem atual' : kma,
        'Tipo de combustível' : tipoc,
        '' : p1,
        '' : p2
       
    }
 
def main ():
    carros = []
   
    while True:
        print ("\nMenu")
        print ("1.Inserir dados do veículo")
        print ("2.Mostrar dados do último veículo inserido")
        print ("3.Mostrar todos os veículos cadastrados")
        print ("9.Sair")
       
        opcao = input ("Escolha uma opção")
       
        if ( opcao == "1" ):
            carro = rgcarro()
            carros.append(carro)
        elif (carro == "2" ):
            if ( carro ):
                exibirfc(carros[-1])
            else:
                print ("Nenhum carro registrado")
        elif ( carro == "3" ):
            exibirtc(carros)
        elif ( carro == "9" ):
            print ("Saindo...")
            break
        else:
            print ("Opção inválida")
if ( __name__ == "__main__"):
    main()