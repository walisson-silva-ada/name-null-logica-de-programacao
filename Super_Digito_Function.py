def concatena(n,k): 
    if k == 1:         
        return(n) 
    return (n + concatena(n, k-1)) 
 
def super_digit(p): 
    lista = list(p) 
    nova_lista = [int(numero) for numero in lista] 
    soma = sum(nova_lista) 
    if soma > 10: 
        return super_digit(str(soma)) 
    else: 
        print(soma)
        return (soma) 
        
 
n, k = input('Insira aqui o número x que deseja '), int(input('Insira a quantidade k de vezes desse número ')) 
p = concatena(n,k)         
super_digit(p)