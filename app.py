# --------------------------------------------------
# IMPORTAÇÕES
# --------------------------------------------------

from flask import Flask, render_template, request, redirect, url_for
import sqlite3


# --------------------------------------------------
# CRIA A APLICAÇÃO FLASK
# --------------------------------------------------

app = Flask(__name__)


# Nome do banco de dados
DATABASE = "database.db"


# --------------------------------------------------
# ROTA DA PÁGINA INICIAL
# --------------------------------------------------

@app.route("/")
def index():

    # Abre uma conexão com o banco de dados
    with sqlite3.connect(DATABASE) as conn:

        # Permite acessar as colunas pelo nome
        conn.row_factory = sqlite3.Row

        # Busca todos os conteúdos ativos
        contents = conn.execute("""
            SELECT
                c_id,
                c_title,
                c_text,
                c_created_at
            FROM content
            WHERE c_status = 'on'
            ORDER BY c_created_at DESC
        """).fetchall()

    # Envia os conteúdos para o index.html
    return render_template(
        "index.html",
        contents=contents
    )


# --------------------------------------------------
# ROTA PARA VISUALIZAR UM CONTEÚDO
# --------------------------------------------------

@app.route("/view/<int:c_id>")
def view(c_id):

    # Abre uma conexão com o banco de dados
    with sqlite3.connect(DATABASE) as conn:

        # Permite acessar as colunas pelo nome
        conn.row_factory = sqlite3.Row

        # Busca somente o conteúdo correspondente ao ID
        content = conn.execute("""
            SELECT
                c_id,
                c_title,
                c_text,
                c_created_at
            FROM content
            WHERE c_id = ?
              AND c_status = 'on'
        """, (c_id,)).fetchone()

    # Caso o conteúdo não seja encontrado
    if content is None:
        return "Conteúdo não encontrado.", 404

    # Envia o conteúdo para view.html
    return render_template(
        "view.html",
        content=content
    )


# --------------------------------------------------
# ROTA PARA CADASTRAR UM NOVO CONTEÚDO
# --------------------------------------------------

@app.route("/new", methods=["GET", "POST"])
def new():

    # Verifica se o formulário foi enviado
    if request.method == "POST":

        # Recebe os dados do formulário
        title = request.form["title"]
        text = request.form["text"]

        # Abre conexão com o banco de dados
        with sqlite3.connect(DATABASE) as conn:

            # Insere o novo conteúdo
            conn.execute("""
                INSERT INTO content (
                    c_title,
                    c_text
                )
                VALUES (?, ?)
            """, (title, text))

            # Confirma a alteração
            conn.commit()

        # Depois do cadastro, volta para a página inicial
        return redirect(url_for("index"))

    # Se for GET, exibe o formulário
    return render_template("new.html")


# --------------------------------------------------
# ROTA PARA EDITAR UM CONTEÚDO
# --------------------------------------------------

@app.route("/edit/<int:c_id>", methods=["GET", "POST"])
def edit(c_id):

    # Abre conexão com o banco de dados
    with sqlite3.connect(DATABASE) as conn:

        # Permite acessar as colunas pelo nome
        conn.row_factory = sqlite3.Row

        # Busca o conteúdo pelo ID
        content = conn.execute("""
            SELECT
                c_id,
                c_title,
                c_text,
                c_created_at
            FROM content
            WHERE c_id = ?
              AND c_status = 'on'
        """, (c_id,)).fetchone()

        # Caso o conteúdo não exista
        if content is None:
            return "Conteúdo não encontrado.", 404

        # Verifica se o formulário foi enviado
        if request.method == "POST":

            # Recebe os novos dados
            title = request.form["title"]
            text = request.form["text"]

            # Atualiza o conteúdo
            conn.execute("""
                UPDATE content
                SET
                    c_title = ?,
                    c_text = ?
                WHERE c_id = ?
            """, (title, text, c_id))

            # Confirma a alteração
            conn.commit()

            # Volta para a página do conteúdo
            return redirect(
                url_for("view", c_id=c_id)
            )

    # Exibe o formulário de edição
    return render_template(
        "edit.html",
        content=content
    )


# --------------------------------------------------
# ROTA PARA EXCLUIR / DESATIVAR UM CONTEÚDO
# --------------------------------------------------

@app.route("/delete/<int:c_id>", methods=["POST"])
def delete(c_id):

    # Abre conexão com o banco de dados
    with sqlite3.connect(DATABASE) as conn:

        # Desativa o conteúdo
        conn.execute("""
            UPDATE content
            SET c_status = 'off'
            WHERE c_id = ?
        """, (c_id,))

        # Confirma a alteração
        conn.commit()

    # Depois da exclusão, volta para a página inicial
    return redirect(url_for("index"))


# --------------------------------------------------
# ROTA DA PÁGINA SOBRE
# --------------------------------------------------

@app.route("/about")
def about():

    return render_template("about.html")


# --------------------------------------------------
# ROTA DA PÁGINA CONTATOS
# --------------------------------------------------

@app.route("/contacts")
def contacts():

    return render_template("contacts.html")


# --------------------------------------------------
# INICIALIZA A APLICAÇÃO
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)