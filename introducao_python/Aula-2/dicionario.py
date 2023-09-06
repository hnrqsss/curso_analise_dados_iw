# Criando dicionario
dados_cliente={
    "Nome": "Renan",
    "Endereco": "Rua 1",
    "Telefone": "987778977"
}

# Alterando dado de uma chave específica
dados_cliente['Telefone'] = '8888888'

# Removendo uma chave específica
dados_cliente.pop('Telefone')

# imprimir dicionario
print(dados_cliente)

# imprimir uma chave específica do dicionario
print(dados_cliente['Nome'])

# Imprimir tipo do dado
print(type(dados_cliente["Nome"]))
print(type(dados_cliente))