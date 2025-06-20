# ======== queries.py ============== #

from db.connect import *


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
    print(f"Conectando ao banco: {DATABASE}@{HOST}:{PORT} como {USER}")

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
