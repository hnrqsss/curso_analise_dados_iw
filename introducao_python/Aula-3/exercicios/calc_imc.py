def calc_imc(peso, altura):
    return peso/altura**2

def indice_imc(imc):
    if imc >= 40:
        return 'Obesidade III'
    elif imc >= 35:
        return 'Obesidade II'
    elif imc >= 30:
        return 'Obesidade I'
    elif imc >= 25:
        return 'Sobrepeso'
    elif imc >= 18.5:
        return 'Normal'
    else:
        return 'Magreza'

nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = calc_imc(peso, altura)
imc_arredondado = round(imc, 2)

indice = indice_imc(imc)

response = ('Nome {} \nIMC: {}\nIndice: {}').format(nome, imc_arredondado, indice)

print(response)