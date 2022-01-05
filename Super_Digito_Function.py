# def concatena(n,k):
#     if k == 1:        
#         return(n)
#     return (str(n) + ' ' + (concatena( str(n), k-1)))

    
# print(concatena(9875,4))
# teste1 = concatena(9875,4)

# str(9875) * 4 
# str(n) * k 
# n = 9875
# k = 4
# nova = str(n) + ' '
# nova*k


# def super_digit(n,k):
#     nova = (str(n) + ' ')*k
#     while k != 1:
#         nova = str(n) * k
#         k -= 1
#     lista = list(nova.replace(" ",""))
#     #print(lista)
#     nova_lista = []
#     for elemento in lista:
#         nova_lista.append((int(elemento)))
#         soma = sum(nova_lista)
#     if soma > 10:
#         return super_digit(str(soma))
#     else:
#         print(soma)
#         return (soma)
        
#super_digit(n,k)

# def sum_of_digit( p ):
#     if p == 0:
#         return 0

#     return (p % 10 + sum_of_digit(int(p / 10)))

# print(sum_of_digit(p))
n= str(input('Insira o número '))
k= int(input('Insira a quantidade de vezes '))
p = list(n*k)
print(p)
def soma_dos_digitos(p):
    soma = 0
    if len(p) > 1:
        for elemento in p:
            inteiro = int(elemento)
            soma += inteiro
            return soma_dos_digitos(soma)
    print(soma)
    return(soma)
soma_dos_digitos(p)


# lista = list(p)
# nova_lista = []
# for elemento in lista:
#     nova_lista.append(int(elemento))
#     soma = sum(nova_lista)

# for elemento in lista:
#          nova_lista.append((int(elemento)))
#          soma = sum(nova_lista)