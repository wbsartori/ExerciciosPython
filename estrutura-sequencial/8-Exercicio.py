""" 
    Faça um Programa que pergunte quanto você ganha por hora 
    e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês. """

mes       = str(input('Digite o mes: '))
valorHora = float(input('Valor da hora: '))
horasMes  = float(input('Horas trabalhadas no mes: ')) 
resultado = valorHora * horasMes

print('O Total do seu salario no mes de {} é de R$ {:.2f} reais.' .format(mes, resultado))