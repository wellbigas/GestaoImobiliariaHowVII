from classes import Pagamento


def consultar_pagamento(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pagamento")
    linhas = cursor.fetchall()
    cursor.close()

    resultado = []
    for linha in linhas:
        resultado.append(Pagamento(linha[0], linha[1], linha[2], linha[3]))

    return resultado

