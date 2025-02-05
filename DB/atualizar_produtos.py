import mysql.connector

def update_product(product_id, new_name, new_price, new_category, new_description, new_image_url):
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
            query = """
            UPDATE produtos
            SET nome = %s, preco = %s, categoria = %s, descricao = %s, imagem_url = %s
            WHERE id = %s
            """
            data = (new_name, new_price, new_category, new_description, new_image_url, product_id)

            # Executar a consulta
            cursor.execute(query, data)
            conn.commit()
            print(f"Produto com ID {product_id} atualizado com sucesso!")
    except mysql.connector.Error as e:
        print(f"Erro ao atualizar produto: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    # Exemplo: Atualizar o produto com ID 2
    update_product(
        product_id=2,
        new_name="Camiseta Azul",
        new_price=59.90,
        new_category="T-shirts",
        new_description="Camiseta básica azul",
        new_image_url="/imagens/camiseta_azul.jpg"
    )
