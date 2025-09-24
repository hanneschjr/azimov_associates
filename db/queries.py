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
            INSERT INTO advogados (nome_advogado, oab, cpf_advogados)
            VALUES (%s, %s, %s)
            ON CONFLICT (cpf_advogados) DO NOTHING
            ''' 
        cursor.execute(query, (nome, oab, cpf))


def add_proc(nr_processo, empresa, tipo, acao, vara, fase,
             instancia, data_ini, data_fin, concl, venc, 
             adv, cliente, cliente_cpf, descricao):
    with instance_cursor() as cursor:
        query='''
            INSERT INTO processos (nr_processo, empresa, tipo, acao,
            vara, fase, instancia, data_inicial, data_final, processo_concluido,
            processo_vencido, advogado, cliente, cpf_cliente, descricao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (nr_processo) DO NOTHING
            ''' 
        cursor.execute(query, (nr_processo, empresa, tipo, acao, vara, fase,
             instancia, data_ini, data_fin, concl, venc, 
             adv, cliente, cliente_cpf, descricao))