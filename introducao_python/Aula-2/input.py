from datetime import date

nome = input('Qual é seu nome? ')
ano = int(input('Qual é o ano do seu nascimento? '))
ano_atual = date.today().year

idade = ano_atual - ano

print("Olá {} sua idade é {} ".format(nome, idade))