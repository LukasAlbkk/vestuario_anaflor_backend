import requests

# URL do endpoint da API
URL = "http://127.0.0.1:5000/api/add_produto"

# Função para adicionar um produto via requisição HTTP
def adicionar_produto():
    nome = input("Nome do Produto: ")
    preco = input("Preço: ")
    imagem_url = input("URL da Imagem: ")
    categoria = input("Categoria: ")

    # Criando o dicionário com os dados do produto
    produto = {
        "nome": nome,
        "preco": preco,
        "imagem_url": imagem_url,
        "categoria": categoria
    }

    # Enviando a requisição POST para a API Flask
    response = requests.post(URL, json=produto)

    # Captura de erro caso a resposta do servidor esteja vazia
    try:
        resposta_json = response.json()
    except requests.exceptions.JSONDecodeError:
        print("❌ Erro: O servidor não retornou uma resposta JSON válida.")
        print(f"🔍 Resposta do servidor: {response.text}")
        return

    # Verificando a resposta
    if response.status_code == 201:
        print("✅ Produto adicionado com sucesso!")
    else:
        print(f"❌ Erro ao adicionar produto: {resposta_json}")

# Rodar a função
if __name__ == "__main__":
    adicionar_produto()
