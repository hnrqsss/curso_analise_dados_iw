def converter_celsius(temp, type):
    if (type == 'fahrenheit'):
        return (temp*1.8) + 32
    if (type == 'kelvin'):
        return temp + 273
    return temp

def converter_fahrenheit(temp, type):
    if (type == 'kelvin'):
        return ((temp - 32) * 5/9) + 273
    if (type == 'celcius'):
        return (temp - 32)/1.8
    return temp

def converter_kelvin(temp, type):
    if (type == 'celcius'):
        return temp - 273
    if (type == 'fahrenheit'):
        return ((temp - 273)*1.8) + 32
    return temp 


opcao = input('Escolha o tipo da primeira temperatura\n1 - Celsius\n2 - Fahrenheit\n3 - Kelvin: \n')

temp = float(input('Digite o valor da temperatura: '))

type = input('Escolha o tipo da conversão temperatura\n1 - Celsius\n2 - Fahrenheit\n3 - Kelvin: \n')

convert_type = {
    '1': 'celsius',
    '2': 'fahrenheit',
    '3': 'kelvin'
}

response = ''

if (type in convert_type and opcao in convert_type):
    if (opcao == '1'):
        response = converter_celsius(temp, convert_type[type])
    elif (opcao == '2'):
        response = converter_fahrenheit(temp, convert_type[type])
    else:
        response = converter_kelvin(temp, convert_type[type])
    
    print('A conversao de {} {} para {}: {}'.format(temp, convert_type[opcao], convert_type[type], response))
else:
    print('Você escolheu uma opção inválida')