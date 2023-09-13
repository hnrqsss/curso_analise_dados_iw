nota = float(input('Digite sua nota: '))

aprovado = 6
recuperacao = 4.5
status = 'Reprovado'

if (nota >= aprovado):
    status = 'Aprovado'
elif(nota >= recuperacao):
    status = 'de Recuperação'

print('Você está {} !!!'.format(status))