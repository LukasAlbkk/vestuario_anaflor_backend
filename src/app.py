import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "chave_super_secreta"

# ✅ Configuração do MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lucas123@localhost/loja_virtual'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = "static/assets/"  # Onde as imagens serão salvas
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

db = SQLAlchemy(app)

# ✅ Modelo do Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    imagem_url = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)

# ✅ Criar tabelas se não existirem
with app.app_context():
    db.create_all()

# ✅ Função para validar tipos de arquivos permitidos
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    # Obtém os últimos 5 produtos adicionados ao banco de dados
    novidades = Produto.query.order_by(Produto.id.desc()).limit(5).all()
    
    return render_template("index.html", novidades=novidades)


# ✅ Exibir Produtos por Categoria (SEM `categoria.html`)
@app.route("/<categoria>")
def categoria_produtos(categoria):
    categorias_validas = ["vestidos", "t_shirts", "body", "croped", "manga_longa", "shorts"]
    
    if categoria not in categorias_validas:
        return page_not_found(404)

    produtos = Produto.query.filter_by(categoria=categoria).all()
    return render_template(f"{categoria}.html", produtos=produtos)  # Usa os arquivos HTML originais

# ✅ Login do Admin
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        senha_digitada = request.form["senha"]
        senha_correta = os.getenv("ADMIN_PASSWORD", "lucas123")

        if senha_digitada == senha_correta:
            session["admin"] = True
            return redirect(url_for("admin_produtos"))
        else:
            return render_template("login.html", erro="Senha incorreta!")

    return render_template("login.html")

# ✅ Logout do Admin
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))

# ✅ Página do Admin para Gerenciar Produtos
@app.route("/admin")
def admin_produtos():
    if "admin" not in session:
        return redirect(url_for("login"))

    produtos = Produto.query.all()
    return render_template("admin_produtos.html", produtos=produtos)

# ✅ Adicionar Produto
@app.route("/add_produto", methods=["GET", "POST"])
def add_produto():
    if "admin" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        categoria = request.form["categoria"]
        imagem = request.files["imagem"]

        if imagem and allowed_file(imagem.filename):
            filename = secure_filename(imagem.filename)
            caminho_imagem = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            imagem.save(caminho_imagem)

            novo_produto = Produto(
                nome=nome,
                preco=float(preco),
                imagem_url=f"/static/assets/{filename}",
                categoria=categoria
            )
            db.session.add(novo_produto)
            db.session.commit()

            return redirect(url_for("admin_produtos"))

    return render_template("add_produto.html")

# ✅ Editar Produto
@app.route("/editar_produto/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    if "admin" not in session:
        return redirect(url_for("login"))

    produto = Produto.query.get_or_404(id)

    if request.method == "POST":
        produto.nome = request.form["nome"]
        produto.preco = request.form["preco"]
        produto.categoria = request.form["categoria"]

        imagem = request.files.get("imagem")
        if imagem and allowed_file(imagem.filename):
            filename = secure_filename(imagem.filename)
            caminho_imagem = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            imagem.save(caminho_imagem)
            produto.imagem_url = f"/static/assets/{filename}"

        db.session.commit()
        return redirect(url_for("admin_produtos"))

    return render_template("editar_produto.html", produto=produto)

# ✅ Rota para deletar um produto
@app.route("/deletar_produto/<int:id>", methods=["POST"])
def deletar_produto(id):
    if "admin" not in session:
        return redirect(url_for("login"))  # Redireciona para login se não estiver autenticado

    produto = Produto.query.get(id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
        return redirect(url_for("admin_produtos"))  # Atualiza a lista de produtos

    return "Produto não encontrado", 404


# ✅ Sistema de Busca
@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("q", "").strip()
    produtos = Produto.query.filter(Produto.nome.ilike(f"%{termo}%")).all()
    return render_template("buscar.html", produtos=produtos, termo=termo)

# ✅ Página 404 Personalizada
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# ✅ Executar o Servidor
if __name__ == "__main__":
    app.run(debug=True)
