import psycopg2
from contextlib import contextmanager
from dotenv import load_dotenv
import os
# o "cursor" é um objeto que permite que você execute comandos SQL no banco de dados e recupere os resultados.
#  Ele age como um ponteiro ou um marcador de posição dentro de uma transação ativa no banco de dados. 
# O cursor permite que você envie consultas SQL para o banco de dados, recuperar os resultados dessas consultas e, em seguida, 
# realizar operações como inserção, atualização e exclusão de dados.

load_dotenv()
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")

if None in [DATABASE, HOST, USER, PASSWORD, PORT]:
    raise ValueError("Erro: Certifique-se de que todas as variáveis de ambiente estão definidas corretamente!")


@contextmanager
def instance_cursor():
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            database=DATABASE,
            host=HOST,
            user=USER,
            password=PASSWORD,
            port=PORT
        )
        cursor = connection.cursor()
        yield cursor  # Aqui, o código que chama essa função executa queries por causa do context
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
        


