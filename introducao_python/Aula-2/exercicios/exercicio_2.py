# Lista de dicionarios de pessoa
pessoas = [
    {
        "Nome": "Henrique",
        "Ano_nascimento": "1990",
        "Compras": [10.20, 20, 40.70, 50],
    },
    {
        "Nome": "Fulano",
        "Ano_nascimento": "1985",
        "Compras": [10, 100.45, 80.11, 51],
    },
    {
        "Nome": "Ciclano",
        "Ano_nascimento": "2000",
        "Compras": [33, 44, 99, 100],
    },
]

# Desafio imprimir os dados e média das compras de cada pessoa e fazer a pesquisa da pessoa pro nome

def calcular_media(compras):
    soma = 0

    for num in compras:
        soma = soma + num 

    media = soma/len(compras)
    
    return media

def calcular_idade(ano_nascimento):
    ano_atual = 2023
    return ano_atual - ano_nascimento

def mostrar_pessoa(pessoa):
    media = calcular_media(pessoa['Compras'])
    idade = calcular_idade(int(pessoa["Ano_nascimento"]))
    print('---------------------------\n')
    print("Nome: {}\nIdade: {}\nMédia das compras: {}\n".format(pessoa['Nome'], idade, media))

def encontrar_pessoa_por_nome(nome, pessoas):
    pessoa = None

    for item in pessoas:
        if (item['Nome'] == nome):
            pessoa = item

    if (pessoa is not None):
        print('---------------------------\n')
        print('\n{} encontrado/a\n'.format(nome))
        
        mostrar_pessoa(pessoa)
    else:
        print('---------------------------\n')
        print('{} não encontrado/a'.format(nome))
            

for pessoa in pessoas:
    mostrar_pessoa(pessoa)

encontrar_pessoa_por_nome('Jovem', pessoas)    