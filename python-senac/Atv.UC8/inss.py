print("---------------------")
print(".::Cálculo de INSS::.")
print("---------------------")

scon = 0
vt = 0
opcao = 0
while(opcao != 9):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")
    scon = float(input("Salário de contribuição: "))
    vt = scon * 0.06


    import os
    os.system ('cls')

    print("---------------------")
    print(".::Cálculo de INSS::.")
    print("---------------------")
    print("Nome: ", nome)
    print("CPF: ", cpf)
    print("Cargo: ", cargo)
    print(f'Desconto de VT: {vt:.2f}')
    print("Salário de contribuição: ", scon)


    if (scon <= 1302):
        scal = (scon / 100) * 7.5
        print(f'Sua contribuição é de {scal:.2f}')
    elif (scon >= 1302.1) and (scon <= 2371.29):
        scal = (scon / 100) * 9
        print('Sua contribuição é de', scal)
    elif (scon >= 2371.30) and (scon <= 3856.94):
        scal = (scon / 100) * 12
        print('Sua contribuição é de', scal)
    elif (scon >= 3856.95) and (scon <= 7507.49):
        scal = (scon / 100) * 14
        print('Sua contribuição é de', scal)

    if (scon <= 1302):
        print("Sua alíquota é de 7.5%.")
    elif (scon >= 1302.1) and (scon <= 2371.29):
        print("Sua alíquota é de 9%.")
    elif (scon >= 2371.30) and (scon <= 3856.94):
        print("Sua alíquota é de 12%.")
    elif (scon >= 3856.95) and (scon <= 7507.49):
        print("Sua alíquota é de 14%.")

    opcao = int(input("Digite 1 para continuar e 9 para sair: "))
if (opcao == 9):
    opcao = 9
    print("OK! Saindo...")

