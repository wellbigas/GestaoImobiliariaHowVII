from classes import Pagamento, EstruturaAnalogica

consulta_1 = 'SELECT p.id_pagamento,p.data_pagamento,p.valor_pagamento,i.id_imovel,i.descricao_imovel,ti.nome_tipo_imovel ' \
        'FROM pagamento p ' \
        'JOIN imovel i ON p.codigo_imovel = i.id_imovel ' \
        'JOIN tipo_imovel ti ON i.tipo_imovel_id = ti.id_tipo_imovel;'


def consultar_pagamento(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pagamento")
    linhas = cursor.fetchall()
    cursor.close()

    resultado = []
    for linha in linhas:
        resultado.append(Pagamento(linha[0], linha[1], linha[2], linha[3]))

    return resultado

def consultar_estrutura_analogica(conexao):
    cursor = conexao.cursor()
    cursor.execute(consulta_1)
    linhas = cursor.fetchall()
    cursor.close()

    resultado = []
    for linha in linhas:
        resultado.append(EstruturaAnalogica(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5]))

    return resultado