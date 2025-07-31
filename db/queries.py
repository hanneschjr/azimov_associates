# ======== queries.py ============== #

from db.connect import *


# def consulta(user):
#     with instance_cursor() as cursor:
#         query= '''
#                 SELECT nome, usuario, senha 
#                 FROM REGISTROS
#                 WHERE usuario = %s   
#             '''
#         cursor.execute(query, (user, ))
#         request = cursor.fetchall()
#         return request

def consulta_geral_advogados():
    with instance_cursor() as cursor:
        query= '''
                SELECT * 
                FROM advogados   
            '''
        cursor.execute(query, )
        request = cursor.fetchall()
        return request

def consulta_geral_processos():
    with instance_cursor() as cursor:
        query= '''
                SELECT * 
                FROM processos   
            '''
        cursor.execute(query, )
        request = cursor.fetchall()
        return request


def add_adv(nome, oab, cpf):
    with instance_cursor() as cursor:
        query='''
            INSERT INTO advogados (advogado, oab, cpf_advogados)
            VALUES (%s, %s, %s)
            ON CONFLICT (oab) DO NOTHING
            ''' 
        cursor.execute(query, (nome, oab, cpf))


