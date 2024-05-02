nomes = ['gustavo' , 'ana' , 'edneia' , 'euler' , 'guilherme']
 
dado = input("Digite seu nome:").upper() #todas as letras ficarem maiúsculas e () é obrigatório
teste = 0                               #title deixa só a primeira leta maiúscula e () é obrigatório
for nome in nomes:
    tnome = nome.upper()
    if tnome == dado:
        print("Nomes são iguais")
        teste = 1
if teste != 1:
    print("Os nomes não são iguais")
 