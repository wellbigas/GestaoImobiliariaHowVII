from manipularBancoDeDados import consultar_pagamento, consultar_estrutura_analogica, \
    calcular_soma_pagamentos_por_imovel, calcular_total_vendas_por_mes_ano, calcular_percentual_vendas_por_tipo_imovel
from dbConection import get_db_connection
from flask import Flask, jsonify


def main():
    try:
        connection = get_db_connection()
        if connection is not None:
            resultados = consultar_estrutura_analogica(connection)

            if resultados is not None:
                for estrutura_analogica in resultados:
                    print(estrutura_analogica)
            else:
                print("Nenhum resultado encontrado.")
        else:
            print("Falha ao estabelecer a conexão com o banco de dados.")

    except Exception as e:
        print(f"Erro geral: {e}")
    finally:
        if connection:
            connection.close()

app = Flask(__name__)


# Rota para calcular a soma de todos os pagamentos por imóvel
@app.route('/soma_pagamentos_por_imovel', methods=['GET'])
def get_soma_pagamentos_por_imovel():
    global connection
    try:
        connection = get_db_connection()
        if connection is not None:
            resultado = calcular_soma_pagamentos_por_imovel(connection)

            if resultado is not None:
                return jsonify(resultado)  # Retorna todo o resultado como JSON
            else:
                print("Nenhum resultado encontrado.")
        else:
            print("Falha ao estabelecer a conexão com o banco de dados.")

    except Exception as e:
        print(f"Erro geral: {e}")
    finally:
        if connection:
            connection.close()



# Rota para calcular o total de vendas por mês/ano
@app.route('/total_vendas_por_mes_ano', methods=['GET'])
def get_total_vendas_por_mes_ano():
    global connection
    try:
        connection = get_db_connection()
        if connection is not None:
            resultado = calcular_total_vendas_por_mes_ano(connection)

            if resultado is not None:
                return jsonify(resultado)  # Retorna todo o resultado como JSON
            else:
                print("Nenhum resultado encontrado.")
        else:
            print("Falha ao estabelecer a conexão com o banco de dados.")

    except Exception as e:
        print(f"Erro geral: {e}")
    finally:
        if connection:
            connection.close()

# Rota para calcular o valor percentual de vendas por tipo de imóvel
@app.route('/percentual_vendas_por_tipo_imovel', methods=['GET'])
def get_percentual_vendas_por_tipo_imovel():
    try:
        connection = get_db_connection()
        if connection is not None:
            resultado = calcular_percentual_vendas_por_tipo_imovel(connection)

            if resultado is not None:
                return jsonify(resultado)  # Retorna todo o resultado como JSON
            else:
                print("Nenhum resultado encontrado.")
        else:
            print("Falha ao estabelecer a conexão com o banco de dados.")

    except Exception as e:
        print(f"Erro geral: {e}")
    finally:
        if connection:
            connection.close()



if __name__ == '__main__':
    app.run(debug=True)
