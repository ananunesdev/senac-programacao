def calcul_terreno (largura1, largura2, comprimentoA, comprimentoB):
    area = ((largura1 + largura1)/2) * ((comprimentoA + comprimentoB)/2)
    return area

larguraE = float(input('Digite a largura da esquerda em metros: '))
larguraD = float(input('Digite a largura da direita em metros: '))

comprimento_entrada = float(input('Digite o comprimento de entrada: '))
comprimento_fundo = float(input('Digite o comprimento de fundo: '))

area_terreno = calcul_terreno(larguraE, larguraD, comprimento_entrada, comprimento_fundo)
print(f'O valor da área: {area_terreno:.2f}m²')

def metros_cubicos (area, altura):
    m3 = area * altura
    return m3

alt_laje = float(input('Digite a altura da laje: '))

alt_laje_m3 = metros_cubicos(area_terreno,alt_laje)

print(f'O valor da área em m³: {alt_laje_m3:.2f}m³')

calc_areia = (alt_laje_m3 / 3) * 2
calc_brita = (alt_laje_m3 / 2) * 2
calc_cimento = (alt_laje_m3 / 1) * 2
calc_peso_caminhao = (alt_laje_m3 * 2400)
total_calc = calc_areia + calc_brita + calc_cimento

print(f'===== MEDIDA PARA CARREGAMENTO DO CAMINHÃO =====')
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

print( '====== CÁLCULO DE LUCRO =====' )
Vareia = 189.03
Vbrita = 175
Vcimento = 270

resultado_areia = ((Vareia / 12) * 6)
resultado_brita = ((Vbrita / 12) * 4)
resultado_cimento = ((Vcimento / 12) * 2)
venda = float(530 * total_calc)

valor_producao = resultado_areia + resultado_brita + resultado_cimento
lucro = venda - valor_producao

print()
print(f'O valor da areia é {resultado_areia:.2f}\n'
f'O valor da brita é {resultado_brita:.2f}\n'
f'O valor da cimento é {resultado_cimento:.2f}\n'
f'Preço de produção {valor_producao:.2f}\n'
f'O valor da venda é {venda:.2f}\n'
f'O lucro é de {lucro:.2f}')


