idade = int(input('Digite sua idade: '))
genero = input('Digite seu gênero M - Masculino ou F - Feminino: ')

status = 'Não é debutante'

if genero == 'F' and idade == 15:
    status = 'Debutante'

print(status)