import mysql.connector

def delete_product(product_id):
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
            query = "DELETE FROM produtos WHERE id = %s"
            data = (product_id,)

            # Executar a consulta
            cursor.execute(query, data)
            conn.commit()
            print(f"Produto com ID {product_id} excluído com sucesso!")
    except mysql.connector.Error as e:
        print(f"Erro ao excluir produto: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    # Exemplo: Excluir o produto com ID 1
    delete_product(product_id=1)
