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

areia = 6 
brita = 4
cimento = 2

total_material = [6, 4, 2]

for material in total_material:
    material_total = alt_laje * len(total_material)
    print('Material total usado na obra: ', material_total)
