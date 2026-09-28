from flask import Flask, jsonify, render_template, request

from livraria import Livraria

app = Flask(__name__)

# Catálogo inicial de livros conforme a especificação
LIVROS_INICIAIS = [
    {
        "id": 1,
        "titulo": "O Hobbit",
        "autor": "J. R. R. Tolkien",
        "preco": 59.90,
        "edicao": "Capa dura",
        "estoque": 5,
    },
    {
        "id": 2,
        "titulo": "Clean Code: Habilidades Práticas do Agile Software",
        "autor": "Robert C. Martin",
        "preco": 89.90,
        "edicao": "1ª edição",
        "estoque": 4,
    },
    {
        "id": 3,
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "preco": 119.90,
        "edicao": "2ª edição",
        "estoque": 6,
    },
    {
        "id": 4,
        "titulo": "O Senhor dos Anéis: A Sociedade do Anel",
        "autor": "J. R. R. Tolkien",
        "preco": 69.90,
        "edicao": "Edição Especial",
        "estoque": 3,
    },
    {
        "id": 5,
        "titulo": "Entendendo Algoritmos",
        "autor": "Aditya Y. Bhargava",
        "preco": 64.90,
        "edicao": "1ª edição",
        "estoque": 8,
    },
    {
        "id": 6,
        "titulo": "O Programador Pragmático: De Aprendiz a Mestre",
        "autor": "Andrew Hunt e David Thomas",
        "preco": 94.50,
        "edicao": "Edição Comemorativa",
        "estoque": 5,
    },
]

livraria = Livraria(LIVROS_INICIAIS)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/livros", methods=["GET"])
def api_livros():
    q = request.args.get("q")
    if q is not None and q.strip() != "":
        livros = livraria.pesquisar_livros(q)
    else:
        livros = livraria.listar_livros()
    return jsonify(livros), 200


@app.route("/api/clientes", methods=["POST"])
def api_cadastrar_cliente():
    data = request.get_json(silent=True) or {}
    nome = data.get("nome")
    email = data.get("email")

    try:
        cliente = livraria.cadastrar_cliente(nome, email)
        return jsonify(cliente), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@app.route("/api/carrinho", methods=["GET"])
def api_visualizar_carrinho():
    carrinho = livraria.visualizar_carrinho()
    return jsonify(carrinho), 200


@app.route("/api/carrinho", methods=["POST"])
def api_adicionar_carrinho():
    data = request.get_json(silent=True) or {}
    livro_id = data.get("livro_id")
    quantidade = data.get("quantidade", 1)

    try:
        if isinstance(quantidade, bool) or quantidade is None:
            raise ValueError("A quantidade deve ser um número inteiro maior que zero.")
        if isinstance(quantidade, float):
            raise ValueError("A quantidade deve ser um número inteiro maior que zero.")
        quantidade_int = int(quantidade)
        item = livraria.adicionar_ao_carrinho(livro_id, quantidade_int)
        return jsonify(item), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@app.route("/api/carrinho/<livro_id>", methods=["DELETE"])
def api_remover_carrinho(livro_id):
    try:
        livraria.remover_do_carrinho(livro_id)
        return jsonify({
            "mensagem": "Livro removido do carrinho.",
            "carrinho": livraria.visualizar_carrinho(),
        }), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@app.route("/api/desejos", methods=["GET"])
def api_listar_desejos():
    desejos = livraria.listar_desejos()
    return jsonify(desejos), 200


@app.route("/api/desejos/<livro_id>", methods=["POST"])
def api_adicionar_desejo(livro_id):
    try:
        desejos = livraria.adicionar_aos_desejos(livro_id)
        return jsonify(desejos), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@app.route("/api/pedidos", methods=["POST"])
def api_finalizar_pedido():
    data = request.get_json(silent=True) or {}
    forma_pagamento = data.get("forma_pagamento")
    modalidade = data.get("modalidade")
    endereco = data.get("endereco")
    loja = data.get("loja")

    try:
        pedido = livraria.finalizar_compra(
            forma_pagamento=forma_pagamento,
            modalidade=modalidade,
            endereco=endereco,
            loja=loja,
        )
        return jsonify(pedido), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
