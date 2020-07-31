"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

"""
v_idade  = []
v_altura = []
v_idade_r  = []
v_altura_r = []

for i in range(5):

    print('Pessoa {}: '.format(i + 1))
    idade  = int(input('Idade: '))
    altura = float(input('Altura: '))
    v_idade.append(idade)    
    v_altura.append(altura)    
    

print('-------------------------------')
print('Idade  = {}'.format(v_idade))
print('Altura = {}'.format(v_altura))
print('Idade  = {}'.format(sorted(v_idade, reverse=True)))
print('Altura = {}'.format(sorted(v_altura, reverse=True)))