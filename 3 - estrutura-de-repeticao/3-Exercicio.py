"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

"""
import os
import sys
import platform
import time


while(1):
    print('##################################################')
    print('### Insira os dados abaixo para se cadastrar: ####')
    print('')
    nome            = str(input('Digite seu nome: '))
    idade           = int(input('Digite sua idade: '))
    salario         = float(input('Digite seu salario: '))
    sexo            = str(input('Digite o sexo: '))
    estadoCivil     = str(input('Digite seu estado civil: '))

    if(len(nome) <= 3):
        print('O nome não pode ter apenas 3 caracteres.')
    elif(idade < 0 or idade > 150):
        print('A idade não esta entre 0 e 150 anos.')
    elif(salario < 0):
        print('O salario deve ser maior que 0.')
    elif(sexo.upper() != 'M' and sexo.upper() != 'F'):
        print('Sexo deve ser M - Masculino ou F - Feminino.')
    elif(estadoCivil.upper() != 'S' and estadoCivil.upper() != 'C' and estadoCivil.upper() != 'V' and estadoCivil.upper() != 'D'):
        print('Estado Civil deve ser:.')
        print('S - Solteiro     (a).')
        print('C - Casado       (a).')
        print('V - Viuvo        (a).')
        print('D - Divorciado   (a).')        
    else:
        if (platform.system() == 'Windows'):
            os.system('cls')
        else:    
            os.system('clear')

        print('##################################################')
        print('NOME: {}'.format(nome.upper()))
        print('IDADE: {}'.format(idade))
        print('SALARIO: R$ {:.2f}'.format(salario))
        print('SEXO: {}'.format(sexo.upper()))
        print('ESTADO CIVIL: {}'.format(estadoCivil.upper()))
        print('Dados cadastrados com sucesso.')
        break

    time.sleep(5)

    if (platform.system() == 'Windows'):
        os.system('cls')
    else:    
        os.system('clear')
