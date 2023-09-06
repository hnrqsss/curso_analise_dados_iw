def soma_compras(compras):
    soma = 0

    for num in compras:
        soma = soma + num 

    return soma

def calcular_media(soma, compras):
    media = soma/len(compras)
    return media

def calcular_idade(ano_nascimento):
    ano_atual = 2023
    return ano_atual - ano_nascimento


# valores das compras
compras = [10.20, 20, 40.70, 50]

# Dicionario pessoa
pessoa = {
    "Nome": "Henrique",
    "Ano_nascimento": "1990",
    "Compras": compras,
}

soma = soma_compras(pessoa['Compras'])
media = calcular_media(soma, pessoa['Compras'])
idade = calcular_idade(int(pessoa["Ano_nascimento"]))

# Desafio imprimir idade e média das compras

resultado = "Idade: {}\nMédia das compras: {}".format(idade, media)

print(resultado)