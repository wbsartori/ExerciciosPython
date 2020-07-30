"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

"""
lista = []
for i in range(10):    
    vetor = str(input('Caracteres {}:  '.format(i+1)))
    lista.append(vetor)
    if(vetor.upper() == 'A' or vetor.upper() == 'E' or vetor.upper() == 'I' or vetor.upper() == 'O' or vetor.upper() == 'U'):        
        lista.remove(vetor)        

print('Consoantes {} .' .format(lista))
print('Total de {} consoantes.'.format(len(lista)))

