import psycopg2
from contextlib import contextmanager
from dotenv import load_dotenv
# import streamlit as st # ative em caso de querer exibir exceções na tela do streamlit!
import os
# o "cursor" é um objeto que permite que você execute comandos SQL no banco de dados e recupere os resultados.
#  Ele age como um ponteiro ou um marcador de posição dentro de uma transação ativa no banco de dados. 
# O cursor permite que você envie consultas SQL para o banco de dados, recuperar os resultados dessas consultas e, em seguida, 
# realizar operações como inserção, atualização e exclusão de dados.

load_dotenv()
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USERSERVER = os.getenv("USERSERVER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")

if None in [DATABASE, HOST, USERSERVER, PASSWORD, PORT]:
    raise ValueError("Erro: Certifique-se de que todas as variáveis de ambiente estão definidas corretamente!")


@contextmanager
def instance_cursor():
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            database=DATABASE,
            host=HOST,
            user=USERSERVER,
            password=PASSWORD,
            port=PORT
        )
        cursor = connection.cursor()
        yield cursor  # Aqui, o código que chama essa função executa queries 
        connection.commit()  # Garante que mudanças sejam salvas no banco
    except Exception as e:
        print(f"Falha ao conectar ao banco de dados: {e}") # aparece no terminal dentro do container

        if connection:
            connection.rollback()  # Evita transações quebradas no banco
        raise RuntimeError("Falha ao conectar ao banco de dados") from e  # Lança um erro mais descritivo na própria aplicação
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print('Conexão com PostgreSQL encerrada')
        

def consulta(user):
    with instance_cursor() as cursor:
        query= '''
                SELECT nome, usuario, senha 
                FROM REGISTROS
                WHERE usuario = %s   
            '''
        cursor.execute(query, (user, ))
        request = cursor.fetchall()
        return request

def consulta_geral():
    with instance_cursor() as cursor:
        query= '''
                SELECT * 
                FROM REGISTROS   
            '''
        cursor.execute(query, )
        request = cursor.fetchall()
        return request

def add_registro(nome, user, senha, email, admin):
    with instance_cursor() as cursor:
        query= f'''
            INSERT INTO REGISTROS VALUES
            {nome, user, senha, email, admin}
            ''' 
        cursor.execute(query)


def cria_tabela():
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USERSERVER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS REGISTROS (
                nome varchar(255),
                usuario varchar(255),
                senha varchar(255),
                email varchar(255),
                admin boolean
            )
        ''' 
        cursor.execute(query)
