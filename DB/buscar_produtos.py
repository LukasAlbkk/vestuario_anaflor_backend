import mysql.connector

def fetch_products():
    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="lucas123",
            database="loja_virtual"
        )
        if conn.is_connected():
            print("Conexão bem-sucedida ao banco de dados!")

            # Criar um cursor para executar a consulta SQL
            cursor = conn.cursor()
            query = "SELECT * FROM produtos"
            cursor.execute(query)

            # Recuperar e exibir os dados
            rows = cursor.fetchall()
            print("Produtos cadastrados:")
            for row in rows:
                print(row)
    except mysql.connector.Error as e:
        print(f"Erro ao consultar produtos: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fetch_products()
