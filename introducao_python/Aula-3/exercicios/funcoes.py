def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    return float(a / b)

def multiplicar(a, b):
    return a * b

menu_opcoes = {
    1: '+',
    2: '-',
    3: 'x',
    4: '/',
}

opcao_escolhida = int(input('Escolha uma opção: \n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n'))

if opcao_escolhida in menu_opcoes:
    resultado = 0

    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    if (opcao_escolhida == 1):
        resultado = soma(a, b)
    elif (opcao_escolhida == 2):
        resultado = subtrair(a, b)
    elif (opcao_escolhida == 3):
        resultado = multiplicar(a, b)
    else:
        resultado = dividir(a, b)
    print('{} {} {} = {}'.format(a, menu_opcoes[opcao_escolhida], b, resultado))

else:
    print('Opção inválida')    

