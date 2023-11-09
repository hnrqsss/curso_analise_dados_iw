import psycopg2 as pg
import uuid


dbname='postgres'
username='root'
password='root'
host='172.17.0.2'
port='5432'

conn = pg.connect(
    database=dbname,
    user=username,
    password=password,
    host=host,
    port=port
)

cur = conn.cursor()

schema = 'crud'

create_schema_sql = 'CREATE SCHEMA {}'.format(schema)
create_customer_table = 'CREATE TABLE {}.clientes (id varchar, nome varchar, idade int)'.format(schema)

# cur.execute(create_schema_sql)
# cur.execute(create_customer_table)

# conn.commit()

print("Sistema de clientes\n")
print("Escolha uma opção\n")
print("1 - Criar cliente \n")
print("2 - Buscar clientes \n")
print("3 - Atualizar cliente \n")
print("4 - Deletar cliente \n")


escolha = input()

def criar_usuario(nome, idade):
    id = str(uuid.uuid4())
    
    query = 'INSERT into crud.clientes (id, nome, idade) VALUES (%s, %s, %s)'

    cur.execute(query, (id, nome, idade))

    conn.commit()

    select_query = 'SELECT * FROM crud.clientes WHERE id = %s'

    cur.execute(select_query, (id,))

    response = cur.fetchone()

    return response

def buscar_clientes(nome):
    select_query = "SELECT * FROM crud.clientes WHERE nome like '%{}%'".format(nome)
    cur.execute(select_query)
    response = cur.fetchall()

    return response

def editar_cliente(id, nome, idade):
    update_query = "UPDATE crud.clientes SET nome='{}', idade='{}' WHERE id = '{}'".format(nome, idade, id)
    cur.execute(update_query)
    conn.commit()

    select_query = 'SELECT * FROM crud.clientes WHERE id = %s'

    cur.execute(select_query, (id,))

    response = cur.fetchone()

    return response

def apagar_cliente(id):
    delete_query = "DELETE from crud.clientes WHERE id = '{}'".format(id)
    cur.execute(delete_query)

    row = cur.rowcount

    conn.commit()

    return 'Cliente deletado com sucesso' if row > 0 else 'Nenhum cliente encontrado'

response = ''

if escolha == '1':
    print("Digite os dados do cliente\n")
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    
    response = criar_usuario(nome=nome, idade=idade)
    
if (escolha == '2'):
    print("Digite o nome do cliente\n")
    nome = input('Nome: ')
    response = buscar_clientes(nome)

if (escolha == '3'):
    print("Digite os dados do cliente\n")
    id = input('ID: ')
    nome = input('Novo nome: ')
    idade = int(input('Nova idade: '))

    response = editar_cliente(id=id, nome=nome, idade=idade)

if (escolha == '4'):
    id = input('Digite o ID do cliente: ')
    
    response = apagar_cliente(id)

print(response)