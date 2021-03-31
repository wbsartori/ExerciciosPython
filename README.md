# ExerciciosPython

### Exemplos de alguns exercicios resolvidos:

```python
print('################################################ 1 ################################################')
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#  Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
#  o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#  salário bruto.
#  quanto pagou ao INSS.
#  quanto pagou ao sindicato.
#  o salário líquido.
#  calcule os descontos e o salário líquido, conforme a tabela abaixo:
#  + Salário Bruto : R$
#  - IR (11%) : R$
#  - INSS (8%) : R$
#  - Sindicato ( 5%) : R$
#  = Salário Liquido : R$
#  Obs.: Salário Bruto - Descontos = Salário Líquido.

print('################################')
print(' CALCULAR DESCONTOS DO SALARIO  ')
print('################################')
print('') 

mes                 = str(input('Digite o mês referencia: '))
valor_por_hora      = float(input('Quanto você ganha por hora ? '))
horas_trabalho_mes  = float(input('Quantas horas você trabalhou no mês ? '))

salario_bruto       = valor_por_hora * horas_trabalho_mes
ir                  = ((11 * salario_bruto) / 100)
inss                = ((8  * salario_bruto) / 100)
sindicato           = ((5  * salario_bruto) / 100)
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print('Salário do Mês de {} '      .format(mes))
print('Salario Bruto    R$ {:.2f} '.format(salario_bruto))
print('IR (11%)         R$ {:.2f} '.format(ir))
print('INSS (8%)        R$ {:.2f} '.format(inss))
print('Sindicato (5%)   R$ {:.2f} '.format(sindicato))
print('Descontos        R$ {:.2f} '.format(descontos))
print('Salário Liquido  R$ {:.2f} '.format(salario_liquido))


print('################################################ 2 ################################################')

""" Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
    sabendo que a decisão é sempre pelo mais barato. """

print('##############################################################')
print('################ PRODUTO COM MENOR VALOR #####################')
print('##############################################################')
print('')

preco_produto_um    = float(input('Informe o preço do produto 1: '))
preco_produto_dois  = float(input('Informe o preço do produto 2: '))
preco_produto_tres  = float(input('Informe o preço do produto 3: '))


if ( preco_produto_um < preco_produto_dois and preco_produto_um < preco_produto_tres):
    print('O produto R$ {:.2f} tem o valor menor que os produtos R$ {:.2f} e R$ {:.2f}.'.format(preco_produto_um, preco_produto_dois, preco_produto_tres))

if ( preco_produto_dois < preco_produto_um and preco_produto_dois < preco_produto_tres):
    print('O produto R$ {:.2f} tem o valor menor que os produtos R$ {:.2f} e R$ {:.2f}.'.format(preco_produto_dois, preco_produto_um,  preco_produto_tres))

if ( preco_produto_tres < preco_produto_dois and preco_produto_tres < preco_produto_um):
    print('O produto R$ {:.2f} tem o valor menor que os produtos R$ {:.2f} e R$ {:.2f}.'.format(preco_produto_tres ,preco_produto_dois, preco_produto_um))


print('################################################ 3 ################################################')

# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

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
´´´
