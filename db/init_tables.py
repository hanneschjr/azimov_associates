# ============ init_tables.py ============ #

from db.connect import *

def create_table_processes():
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS processos (
                nr_processo VARCHAR(20) PRIMARY KEY,
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
                advogado TEXT,
                oab VARCHAR(20) PRIMARY KEY,
                cpf_advogados VARCHAR(11) NOT NULL
            )
        ''' 
        cursor.execute(query)


def create_table_process_lawyer():
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS processo_advogado (
                nr_processo VARCHAR(20),
                oab VARCHAR(20),
                PRIMARY KEY (nr_processo, oab),
                FOREIGN KEY (nr_processo) REFERENCES processos(nr_processo),
                FOREIGN KEY (oab) REFERENCES advogados(oab)
            )
        ''' 
        cursor.execute(query)