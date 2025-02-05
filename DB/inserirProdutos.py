import mysql.connector

def insert_product():
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
            INSERT INTO produtos (nome, preco, categoria, descricao, imagem_url)
            VALUES (%s, %s, %s, %s, %s)
            """
            data = ('Camiseta Vermelha', 69.90, 'T-shirts', 'Camiseta básica vermelha', '/imagens/camiseta_vermelha.jpg')
            
            # Executar a consulta
            cursor.execute(query, data)
            conn.commit()
            print("Produto inserido com sucesso!")
    except mysql.connector.Error as e:
        print(f"Erro ao inserir produto: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    insert_product()
