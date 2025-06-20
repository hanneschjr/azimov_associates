import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

def create_database_if_not_exists():
    target_dbname = os.getenv("DATABASE")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST", "localhost")
    port = os.getenv("PORT", 5432)

    connection = psycopg2.connect(
        dbname="postgres",
        user=user,
        password=password,
        host=host,
        port=port
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # muda a conexão para realizar comandos to tipo CREATE DATABASE - obrigatória
                                                               # executa imediatamente a operação sem precisar de commit manual
    cursor = connection.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (target_dbname,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(f'CREATE DATABASE "{target_dbname}"')
        print(f"Banco de dados '{target_dbname}' criado.")
    else:
        print(f"Banco de dados '{target_dbname}' já existe.")

    cursor.close()
    connection.close()