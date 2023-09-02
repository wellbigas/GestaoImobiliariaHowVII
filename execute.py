from manipularBancoDeDados import consultar_pagamento, consultar_estrutura_analogica
from dbConection import get_db_connection

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

if __name__ == "__main__":
    main()
