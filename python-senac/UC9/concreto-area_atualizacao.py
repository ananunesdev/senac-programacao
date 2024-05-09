def calcular_area_terreno(comprimentofrente, comprimentofundo, larguraesquerda, larguradireita):
    area = ((comprimentofrente + comprimentofundo)/2) * ((larguraesquerda + larguradireita)/2)
    return area

def calcular_area_cubica(area, altura):
    m3 = area * altura
    return m3

comprimento_terreno_frente = float(input('Digite o comprimento de frente do terreno em metros: '))
comprimento_terreno_fundo = float(input('Digite o comprimento de fundo do terreno em metros: '))

largura_terreno_esquedo = float(input('Digite a largura do lodo esquerdo do terreno em metros: '))
largura_terreno_direito = float(input('Digite a largura do lodo direito do terreno em metros: '))

altura_laje_m3 = float(input('Digite a altura da laje Ex.: 0.10 metros: '))

area_terreno = calcular_area_terreno(comprimento_terreno_frente, comprimento_terreno_fundo, largura_terreno_esquedo, largura_terreno_direito)
altura_lj_m3 = calcular_area_cubica(area_terreno, altura_laje_m3)

calc_areia = (altura_lj_m3 / 3) * 2
calc_brita = (altura_lj_m3 / 2) * 2
calc_cimento = (altura_lj_m3 / 1) * 2
calc_peso_caminhao = (altura_lj_m3 * 2400)

comp_areia = 189.03 #valor de metros cubicos
comp_brita = 175.00 #valor de metros cubicos
comp_cimento = 270.00 #valor de metros cubicos

print(f'A media em metros quadrados é: {area_terreno:.2f}.\n')
print(f'A medida em metros cubicos é: {altura_lj_m3:.2f}.\n')

print('===== MEDIDA PARA CARREGAMENTO DO CAMINHÃO =====')
print(f'Qtd.: Areia: {calc_areia:.2f}\n')
print(f'Qtd.: Brita: {calc_brita:.2f}\n')
print(f'Qtd.: Cimento: {calc_cimento:.2f}\n')

print('===== PESO DO CAMINHÃO EM M³ =====\n')
print(f'Peso de Caminhão: {calc_peso_caminhao:.3f}\n')


#Valor de custo de produção areia (189,03) / brita (175,00) / Cimento R$ 270
#Calcular o valor de preço 530 por metros cubicos...

#Base 12
#6 areia       189,03 / 2 = 94,51
#4 brita       175,00 / 3 = 58,33    =  197,84
#2 cimento     270,00 / 6 = 45,00