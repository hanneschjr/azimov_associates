# ============ init_tables.py ============ #

from db.connect import *

def create_tables():
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USER}")

    with instance_cursor() as cursor:
        query= '''
            CREATE TABLE IF NOT EXISTS processos (
                nr_processo INTEGER,
                empresa TEXT,
                tipo TEXT,
                acao TEXT,
                vara TEXT,
                instancia INTEGER,
                data_inicial TEXT, 
                data_final TEXT,
                processo_concluido INTEGER,
                processo_vencido INTEGER,
                advogados TEXT,
                cliente TEXT,
                cpf_cliente INTEGER,
                descricao TEXT,
            )
        ''' 
        cursor.execute(query)