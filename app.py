import os
from dotenv import load_dotenv

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    session
)

from database import (
    listar_marcacoes,
    adicionar_marcacao,
    remover_marcacao,
    autenticar
)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

PONCHO_VERDE = {
    "lat": -28.3051754,
    "lon": -53.5083942
}


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/dados")
def dados():

    return jsonify({

        "problemas": listar_marcacoes("problema"),

        "solucoes": listar_marcacoes("solucao"),

        "escola": PONCHO_VERDE

    })


@app.route("/problema", methods=["POST"])
def problema():

    if "usuario" not in session:

        return {
        "erro": "Não autorizado"
         }, 401

    dados = request.json

    adicionar_marcacao(

        "problema",

        dados["rua"],

        dados["descricao"],

        dados["lat"],

        dados["lon"]

    )

    return {"ok": True}


@app.route("/solucao", methods=["POST"])
def solucao():

    if "usuario" not in session:

        return {
        "erro": "Não autorizado"
        }, 401

    dados = request.json

    adicionar_marcacao(

        "solucao",

        dados["rua"],

        dados["descricao"],

        dados["lat"],

        dados["lon"]

    )

    return {"ok": True}


@app.route("/remover_problema/<int:id>", methods=["DELETE"])
def remover_problema(id):
    if "usuario" not in session:

        return {
        "erro": "Não autorizado"
        }, 401
    remover_marcacao(id)

    return {"ok": True}


@app.route("/remover_solucao/<int:id>", methods=["DELETE"])
def remover_solucao(id):

    if "usuario" not in session:

        return {
        "erro": "Não autorizado"
        }, 401
    remover_marcacao(id)

    return {"ok": True}

@app.route("/login", methods=["POST"])
def login():

    dados = request.json

    usuario = autenticar(
        dados["usuario"],
        dados["senha"]
    )

    if usuario:

        session["usuario"] = dados["usuario"]

        return {
            "ok": True
        }

    return {
        "ok": False
    }, 401

@app.route("/logout")
def logout():

    session.clear()

    return {
        "ok": True
    }

@app.route("/status")
def status():

    return jsonify({

        "logado": "usuario" in session,

        "usuario": session.get("usuario")

    })

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )