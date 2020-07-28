"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite 
a senha igual ao nome do usuário, mostrando uma mensagem de erro e 
voltando a pedir as informações.
"""
import os
import sys
import platform
import time


while(1):
    print('Digite o usuario e senha.')

    nome    = input('Usuario: ')
    senha   = input('Senha: ')
    
    if( nome.upper() == senha.upper()):
        print('Você não pode digitar uma senha com mesmo nome de usuário.')        
        time.sleep(3)

        if (platform.system() == 'Windows'):
            os.system('cls')
        else:    
            os.system('clear')
    else:
        print('Logado com sucesso.')
        time.sleep(3)

        if (platform.system() == 'Windows'):
            os.system('cls')
        else:    
            os.system('clear')
        
        print('SEJA BEM VINDO !')
        time.sleep(2)
        break