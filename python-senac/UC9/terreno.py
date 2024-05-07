def cal_areaT(comprimento, largura):
    area = comprimento * largura
    return area

comprimento_t = float(input('Digite o comprimento do terreno em metros: '))
largura_t = float(input('Digite a largura do terreno em metros: '))

area_t = cal_areaT(comprimento_t, largura_t)
print(f'A área do terreno é: {area_t:.2f} metros quadrados.')