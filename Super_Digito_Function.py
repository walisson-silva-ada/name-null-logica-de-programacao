def super_digito(n,k):
    if k == 1:        
        return(n)

    return (str(n) + ' ' + (super_digito( str(n), k-1)))
print(super_digito(9875,4))
teste1 = super_digito(9875,4)
type(teste1)

numero = teste1
type(numero)
print(numero)
numero.replace(" ","")
print(numero)
#lista = list(numero)
#print(lista)
# nova_lista = []
# for elemento in lista:
#     nova_lista.append((int(elemento)))
#     soma = sum(nova_lista)
# print(soma)


# print(super_digito(9875,4))

# testin = '9875'
# print(list(testin))
# lista = list(testin)
# nova_lista = []
# for elemento in lista:
#     nova_lista.append(int(elemento))
    
# print(nova_lista)
# soma = sum(nova_lista)
# print(soma)

# def super_digito(n,k):
#     while k != 0:
#         #return(n)
#         return(super_digito(str(n) + ' ' + str(n),k-1))
#     return(n)

# print(super_digito(9875,4))

# n = str(9875)
# k = 4
# p = n*4
# print(p)
