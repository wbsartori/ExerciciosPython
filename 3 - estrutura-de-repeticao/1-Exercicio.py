"""
    Faça um programa que peça uma nota, entre zero e dez. 
    Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

while(1):
    valor = int(input('Digite um valor entre 0 e 10: '))
    
    if(valor >= 0 and valor <=10):
        print('O valor {} esta entre 0 e 10.'.format(valor))
        break    