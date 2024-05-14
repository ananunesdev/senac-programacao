import os
from datetime import date
#import time
data = date.today()

clientes = ["Ana"]
fucionarios = ["Eric", "Ana Luiza", "Matheus"]



#MENU INICIAL
def inicio():
    print("\n"f"- - - - - - - - ＡＣＡＤＥＭＩＡ ＦＡＵＳＴＩＮＯ - - - - - - - -   {data}\n")
    print("1- Cadastrar Cliente\n"
          "2- Listar Clientes\n"
          "3- Listar Personal Trainer\n"
          "4- Sair\n")


def cadastrar_Cliente():
    os.system('cls')
    print("- - - 𝖢𝖠𝖣𝖠𝖲𝖳𝖱𝖠𝖬𝖤𝖭𝖳𝖮 𝖣𝖤 𝖢𝖫𝖨𝖤𝖭𝖳𝖤 - - -")   
    nome_New_Cliente = str(input("Insira o nome do cliente: "))
    clientes.append(nome_New_Cliente)
    idade_New_Cliente = int(input("Insira a idade do cliente: "))
    Peso_New_Cliente = float(input("Insira o Peso em kg do cliente: "))
    altura_New_cliente = float(input("insira a altura do cliente: EX: 0.00 : "))
    imc = Peso_New_Cliente / (altura_New_cliente*altura_New_cliente)
        
    os.system('cls\n')
    print("- - - 𝖢𝖠𝖣𝖠𝖲𝖳𝖱𝖮 𝖣𝖤 𝖢𝖫𝖨𝖤𝖭𝖳𝖤 - - -\n"
          f"Nome: {nome_New_Cliente}              Idade: {idade_New_Cliente}\n"
          f"Peso: {Peso_New_Cliente}               Altura:{altura_New_cliente}\n"
          f"IMC: {imc}         Classificação do IMC:") 
    
    input("\nDigite qualquer botão para voltar: ")
    os.system('cls')
    main()
    return nome_New_Cliente, Peso_New_Cliente, altura_New_cliente, idade_New_Cliente
    
def  listar_Clientes():
    os.system('cls')
    i = 0
    for cliente in clientes:
        print(clientes[i]) 
        i = i + 1
    input("\nDigite qualquer botão para voltar: ")
    os.system('cls')
    main()
    
    

def listar_Personal():
    os.system('cls')
    i = 0
    for funcionario in fucionarios:
        print(fucionarios[i]) 
        i = i + 1
    input("\nDigite qualquer botão para voltar: ")
    os.system('cls')
    main()

def finalizar_System():
    os.system('cls')
    print("Programa finalizado, feche-o para sair")
    
def escolher_opcao():
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        cadastrar_Cliente()
    elif opcao == 2:
        listar_Clientes()
    elif opcao == 3:
        listar_Personal()
    elif opcao == 4:
        finalizar_System()
    else:
        os.system('cls')
        inicio()
        print("Escolha uma opção listada acima")
        escolher_opcao()        
 


def main():
    inicio()
    escolher_opcao()
    

if __name__ == '__main__':
    main()