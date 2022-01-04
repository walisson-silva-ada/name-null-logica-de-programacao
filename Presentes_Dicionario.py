# dicionario_presentes = {
# 'iara': ('mochila', 'estojo','lapis'),
# 'adelar': ('sapato', 'camisa', 'carteira'),
# 'jessica': ('agenda', 'bolsa', 'brincos'),
# 'jocelina': ('xicara', 'meias', 'perfume'),
# 'elaine': ('sandalia', 'sapatilha', 'camiseta')

#}
quantidade = int(input('Insira o número de pessoas '))
i = 0
dicionario_presentes = {}
while i < quantidade:
    tudao = input('Insira aqui o nome e os 3 presentes da pessoa')
    valores = tudao.split(' ')
    chave = valores[0]
    valores.pop(0)
    dicionario_presentes[chave] = valores
    i += 1
    
print(dicionario_presentes)



nome_presente = input('insira o nome da pessoa e o presente que deseja dar')
presente = nome_presente.split(' ')
nome = presente[0]
presentinho = presente[1]

print(presente)


if presentinho in dicionario_presentes[nome]:
    
    print('Uhul! Seu amigo secreto vai adorar o/')
else: print('Tente Novamente!')