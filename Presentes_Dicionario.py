# dicionario_presentes = {
# 'iara': ('mochila', 'estojo','lapis'),
# 'adelar': ('sapato', 'camisa', 'carteira'),
# 'jessica': ('agenda', 'bolsa', 'brincos'),
# 'jocelina': ('xicara', 'meias', 'perfume'),
# 'elaine': ('sandalia', 'sapatilha', 'camiseta')

# }

quantidade = int(input('Insira o número de pessoas '))
i = 0
dicionario_presentes = {}
while i < quantidade:
    entrada_info = input('Insira aqui o nome e os 3 presentes da pessoa ')
    valores_separados = entrada_info.split(' ')
    chave = valores_separados[0]
    valores_separados.pop(0)
    dicionario_presentes[chave] = valores_separados
    i += 1
    
print(dicionario_presentes)
nome = [] 
presente = [] 
numero_verificacores = int(input('Insira quantas pessoas quer verificar o presente. '))
n = 0 
while n < numero_verificacores: 

    nome_presente = input('insira o nome da pessoa e o presente que deseja dar ') 
    separado = nome_presente.split(' ') 
    nome.append(separado[0]) 
    presente.append(separado[1]) 
    n += 1 


j = 0
for j in range(len(nome)):
    if presente[j] in dicionario_presentes[nome[j]]:
        print('Uhul! Seu amigo secreto vai adorar o/')
    else: print('Tente Novamente!')



# 5
# iara mochila estojo lapis
# adelar sapato camisa carteira
# jessica agenda bolsa brincos
# jocelina xicara meias perfume
# elaine sandalia sapatilha camiseta
# jessica carteira
# jessica agenda
# iara sandalia
# elaine mochila
# iara mochila
# adelar carteira