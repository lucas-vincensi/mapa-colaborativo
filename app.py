from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

PROBLEMAS = "problemas.json"
SOLUCOES = "solucoes.json"

PONCHO_VERDE = {
    "lat": -28.3051754,
    "lon": -53.5083942
}


def carregar(nome):
    if not os.path.exists(nome):
        return []

    with open(nome, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []


def salvar(nome, dados):
    with open(nome, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dados")
def dados():

    return jsonify({
        "problemas": carregar(PROBLEMAS),
        "solucoes": carregar(SOLUCOES),
        "escola": PONCHO_VERDE
    })


@app.route("/problema", methods=["POST"])
def problema():

    dados = carregar(PROBLEMAS)

    dados.append(request.json)

    salvar(PROBLEMAS, dados)

    return {"ok": True}


@app.route("/solucao", methods=["POST"])
def solucao():

    dados = carregar(SOLUCOES)

    dados.append(request.json)

    salvar(SOLUCOES, dados)

    return {"ok": True}

@app.route("/remover_problema/<int:id>", methods=["DELETE"])
def remover_problema(id):

    dados = carregar(PROBLEMAS)

    dados = [
        p for p in dados
        if p["id"] != id
    ]

    salvar(PROBLEMAS, dados)

    return {"ok": True}


@app.route("/remover_solucao/<int:id>", methods=["DELETE"])
def remover_solucao(id):

    dados = carregar(SOLUCOES)

    dados = [
        s for s in dados
        if s["id"] != id
    ]

    salvar(SOLUCOES, dados)

    return {"ok": True}

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )