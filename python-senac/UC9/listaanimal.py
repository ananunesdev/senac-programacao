ListaAnimais = ['Cão', 'Gato', 'Galinha', 'Coelho']
animal = str(input("Qual seu animal de estimação? "))
idadeh = int(input('Qual a idade humana do seu animal? '))

for especie in ListaAnimais:
    if especie == 'Cão':
        if animal == especie:
            idadeA = idadeh * 7
            print('A idade do seu cachorro é ', idadeA)
    elif especie == 'Gato':
        if animal == especie:
            idadeA = idadeh * 4
            print('A idade do seu gato é ', idadeA)
    elif especie == 'Galinha':    
        if animal == especie:
            idadeA = idadeh * 18
            print('A idade da sua galinha é ', idadeA)
    elif especie == 'Coelho':    
        if animal == especie :
            idadeA = idadeh * 5
            print('A idade do seu coelho é ', idadeA)