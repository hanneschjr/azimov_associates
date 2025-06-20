# ============ init_tables.py ============ #

from db.connect import *

def create_table_processes():
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS processos (
                nr_processo INTEGER PRIMARY KEY,
                empresa TEXT,
                tipo TEXT,
                acao TEXT,
                vara TEXT,
                instancia INTEGER,
                data_inicial DATE, 
                data_final DATE,
                processo_concluido INTEGER,
                processo_vencido INTEGER,
                advogados TEXT,
                cliente TEXT,
                cpf_cliente INTEGER,
                descricao TEXT
            )
        ''' 
        cursor.execute(query)

def create_table_lawyers():
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS advogados (
                advogado TEXT,
                oab INTEGER PRIMARY KEY,
                cpf INTEGER
            )
        ''' 
        cursor.execute(query)