# ============ init_tables.py ============ #

from db.connect import *

def create_table_processes():
    print(f"Criando a tabela 'Processos' no banco: {DATABASE}@{HOST}:{PORT} como {USER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS processos (
                id SERIAL PRIMARY KEY,
                nr_processo VARCHAR(20) UNIQUE,
                empresa TEXT,
                tipo TEXT,
                acao TEXT,
                vara TEXT,
                fase TEXT,
                instancia INTEGER,
                data_inicial DATE, 
                data_final DATE,
                processo_concluido INTEGER,
                processo_vencido INTEGER,
                advogado TEXT,
                cliente TEXT,
                cpf_cliente VARCHAR(11),
                descricao TEXT
            )
        ''' 
        cursor.execute(query)

def create_table_lawyers():
    print(f"Criando a tabela 'Advogados no banco: {DATABASE}@{HOST}:{PORT} como {USER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS advogados (
                id SERIAL PRIMARY KEY,
                nome_advogado TEXT UNIQUE,
                oab VARCHAR(20) NOT NULL UNIQUE,
                cpf_advogados VARCHAR(11) NOT NULL UNIQUE
            )
        ''' 
        cursor.execute(query)
