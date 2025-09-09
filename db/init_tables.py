# ============ init_tables.py ============ #

from db.connect import *

def create_table_processes():
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS processos (
                id SERIAL PRIMARY KEY,
                nr_processo VARCHAR(20) UNIQUE,
                empresa TEXT,
                tipo TEXT,
                acao TEXT,
                vara TEXT,
                instancia INTEGER,
                data_inicial DATE, 
                data_final DATE,
                processo_concluido BOOLEAN,
                processo_vencido BOOLEAN,
                advogados TEXT,
                cliente TEXT,
                cpf_cliente VARCHAR(11),
                descricao TEXT
            )
        ''' 
        cursor.execute(query)

def create_table_lawyers():
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USER}")

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


def create_table_process_lawyer():
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS processos_advogados (
                id SERIAL PRIMARY KEY,
                id_processo INT NOT NULL,
                id_advogado INT NOT NULL,
                FOREIGN KEY (id_processo) REFERENCES processos(id),
                FOREIGN KEY (id_advogado) REFERENCES advogados(id),
                UNIQUE (id_processo, id_advogado)
            )
        ''' 
        cursor.execute(query)