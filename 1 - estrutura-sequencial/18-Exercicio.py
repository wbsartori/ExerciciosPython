""" Faça um programa que peça o tamanho de um arquivo para download (em MB) 
    e a velocidade de um link de Internet (em Mbps), calcule e informe o 
    tempo aproximado de download do arquivo usando este link (em minutos). """


print('#################################################################')
print('########### CALCULAR  VELOCIDADE DOWNLOAD  ######################')
print('#################################################################')
print('') 

velocidade_internet = float(input('Qual a velocidade da sua internet? '))
arquivo_mb = float(input('Informe o tamanho do arquivo em MB: '))

mega = 1024
converter_conexao = ((velocidade_internet * mega) / 8)
converter_unidade = (arquivo_mb * 1024)
segundos  = (converter_unidade / converter_conexao)
minutos = (segundos / 60)

print('')
print('Velocidade da conexão: {:.2f} Mb '.format(velocidade_internet))
print('Tamanho do arquivo:    {:.2f} Mb'.format(arquivo_mb))
print('O tempo de download é de {:.2f} minutos '.format(minutos))
print('Velocidade de download é de {:.2f} Mbps'.format(converter_conexao))




