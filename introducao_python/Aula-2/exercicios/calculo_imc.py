# Criar algoritimo para calcular IMC de uma pessoa recebendo os dados necessários através do input

pessoa = {
    'Nome': '',
    'Peso': '',
    'Altura': '',
}

# peso kg/altura cm ²
pessoa['Nome'] = input('Digite seu nome: ')
pessoa['Peso'] = float(input('Digite seu peso em kg: '))
pessoa['Altura'] = float(input('Digite sua altura em metros: '))

imc = pessoa['Peso']/pessoa['Altura']**2

response = ('Nome {} \nIMC: {}').format(pessoa['Peso'], imc)

print(response)
