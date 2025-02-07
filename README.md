# 🛍️ Ana Flor - Loja Virtual

Este é um projeto de loja virtual desenvolvido com Flask e MySQL, permitindo a administração de produtos através de um painel para o administrador. 

## 🚀 Funcionalidades

- 📌 **Login do administrador** para adicionar, editar e remover produtos.
- 📌 **Cadastro de produtos**, incluindo nome, preço, imagem e categoria.
- 📌 **Exibição dinâmica de produtos**, atualizando automaticamente as novidades.
- 📌 **Sistema de busca** para encontrar produtos cadastrados.
- 📌 **Categorias de produtos** com páginas individuais.
- 📌 **Redirecionamento para WhatsApp** para finalizar a compra.

---

## 🛠️ Tecnologias Utilizadas

- **Python (Flask)** - Framework web para o backend.
- **MySQL** - Banco de dados para armazenar os produtos.
- **HTML, CSS e JavaScript** - Para a interface da loja.
- **Jinja2** - Template engine do Flask.

---

## 🛠️ Configuração do Projeto

### 🔹 1️⃣ Clonar o repositório
Abra o terminal no VSCode e execute:

```bash
git clone https://github.com/seu-usuario/vestuario_anaflor_backend.git
cd vesturario_anaflor_backend/src


🔹 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)

python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

🔹 3️⃣ Instalar dependências

pip install -r requirements.txt

🔹 4️⃣ Configurar o banco de dados MySQL

    Crie um banco de dados no MySQL chamado loja_virtual:

CREATE DATABASE loja_virtual;

    Configure o usuário no MySQL (root no exemplo abaixo, ajuste conforme necessário).

🔹 5️⃣ Executar a aplicação

python app.py

A aplicação rodará em http://127.0.0.1:5000.
📂 Estrutura do Projeto

📁 src
│── 📁 static
│   ├── 📁 assets       # Imagens e arquivos estáticos
│   ├── style.css       # Estilos da aplicação
│── 📁 templates
│   ├── index.html      # Página inicial
│   ├── login.html      # Tela de login do admin
│   ├── add_produto.html # Formulário de adição de produto
│   ├── admin_produtos.html # Painel de administração
│   ├── editar_produto.html # Formulário de edição
│   ├── resultados_busca.html # Resultados da busca
│── app.py              # Código principal do Flask
│── .gitignore          # Arquivos ignorados pelo Git
│── README.md           # Documentação do projeto

🔥 Melhorias Futuras

    📌 Implementar um sistema de carrinho de compras.
    📌 Integração com APIs de pagamento.
    📌 Painel com estatísticas de vendas.

💡 Como contribuir

    Faça um fork do projeto.
    Crie uma branch (git checkout -b minha-feature).
    Faça commit das mudanças (git commit -m 'Minha nova feature').
    Faça um push (git push origin minha-feature).
    Abra um Pull Request.

📝 Licença

Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
📞 Contato

    📸 Instagram: @vestuarioanaflor
    
