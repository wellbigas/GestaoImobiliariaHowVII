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



# Item A - Implementar uma função que retorne uma lista com o id de cada imóvel e sua respectiva soma de todos os pagamentos.
# Função para calcular a soma de todos os pagamentos por imóvel
def calcular_soma_pagamentos_por_imovel(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
            SELECT p.codigo_imovel, p.valor_pagamento
            FROM pagamento p
        """)
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()

    soma_por_imovel = {}

    for codigo_imovel, valor_pagamento in resultados:
        if codigo_imovel not in soma_por_imovel:
            soma_por_imovel[codigo_imovel] = 0
        soma_por_imovel[codigo_imovel] += valor_pagamento

    return soma_por_imovel

# Item B - Função para calcular o total de vendas por mês/ano
def calcular_total_vendas_por_mes_ano(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT data_pagamento, valor_pagamento
        FROM pagamento;
    """)
    resultados = cursor.fetchall()
    cursor.close()

    # Processar os dados na memória
    total_vendas_por_mes_ano = {}
    for data_pagamento, valor_pagamento in resultados:
        mes_ano = data_pagamento.strftime('%m/%Y')
        if mes_ano not in total_vendas_por_mes_ano:
            total_vendas_por_mes_ano[mes_ano] = 0
        total_vendas_por_mes_ano[mes_ano] += valor_pagamento

    # Formatar os resultados
    resultado_formatado = [{"mes_ano": mes_ano, "total_vendas": total_vendas} for mes_ano, total_vendas in total_vendas_por_mes_ano.items()]
    return resultado_formatado

# Função para calcular o valor percentual de vendas por tipo de imóvel
def calcular_percentual_vendas_por_tipo_imovel(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
            SELECT ti.nome_tipo_imovel, p.valor_pagamento
            FROM pagamento p
            JOIN imovel i ON p.codigo_imovel = i.id_imovel
            JOIN tipo_imovel ti ON i.tipo_imovel_id = ti.id_tipo_imovel;
        """)
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()

    vendas_por_tipo_imovel = {}

    for nome_tipo_imovel, valor_pagamento in resultados:
        if nome_tipo_imovel not in vendas_por_tipo_imovel:
            vendas_por_tipo_imovel[nome_tipo_imovel] = 0
        vendas_por_tipo_imovel[nome_tipo_imovel] += valor_pagamento

    total_vendas = sum(vendas_por_tipo_imovel.values())

    percentuais = {tipo_imovel: round((valor / total_vendas) * 100, 2) for tipo_imovel, valor in vendas_por_tipo_imovel.items()}

    return percentuais
