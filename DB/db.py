import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="lucas123",
        database="loja_virtual"
    )

    if conn.is_connected():
        print("Conexão bem-sucedida ao banco de dados!")
except mysql.connector.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
    if conn.is_connected():
        conn.close()
