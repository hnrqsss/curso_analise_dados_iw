# Dicionario pessoa
pessoa = {
    "Nome": "Henrique",
    "Ano_nascimento": "1990",
    "Compras": [10.20, 20, 40.70, 50],
}

# Desafio imprimir idade e média das compras

def calcular_media(compras):
    soma = 0

    for num in compras:
        soma = soma + num 

    media = soma/len(compras)
    
    return media

def calcular_idade(ano_nascimento):
    ano_atual = 2023
    return ano_atual - ano_nascimento

media = calcular_media(pessoa['Compras'])
idade = calcular_idade(int(pessoa["Ano_nascimento"]))

print("Idade: {}\nMédia das compras: {}".format(idade, media))