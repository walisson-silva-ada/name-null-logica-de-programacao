def soma_elementos(lista_p):
    if len(lista_p) == 1:
        return lista_p[0]
    else:
        return lista_p[0] + soma_elementos(lista_p[1:])
n = input('Digite o seu número ')
k = int(input('Digite a quantidade de vezes '))

n_lista = [int(elemento) for elemento in n]
p = n_lista * k 

while len(p) > 1:
    resultado = soma_elementos(p)
    p = [int(numero) for numero in str(resultado)]
print('O super digito é',resultado)
