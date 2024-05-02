nomes = ['gustavo' , 'ana' , 'edneia' , 'euler' , 'guilherme']
 
dado = input("Digite seu nome:").upper() #todas as letras ficarem maiúsculas
teste = 0
for nome in nomes:
    tnome = nome.upper()
    if tnome == dado:
        print("Nomes são iguais")
        teste = 1
if teste != 1:
    print("Os nomes não são iguais")
 