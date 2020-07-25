""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
    o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
    Obs.: Salário Bruto - Descontos = Salário Líquido. """

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