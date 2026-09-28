class Livraria:
    """Domínio principal da Livraria com armazenamento em memória."""

    def __init__(self, livros=None):
        self.livros = [dict(livro) for livro in livros] if livros else []
        self.clientes = []
        self.carrinho = {}
        self.desejos = []
        self.pedidos = []
        self._proximo_cliente_id = 1
        self._proximo_pedido_id = 1

    def _buscar_livro(self, livro_id):
        for livro in self.livros:
            if livro["id"] == livro_id:
                return livro
        return None

    def cadastrar_cliente(self, nome, email):
        if not nome or not str(nome).strip():
            raise ValueError("Nome é obrigatório.")
        if not email or not str(email).strip():
            raise ValueError("E-mail é obrigatório.")

        email_limpo = str(email).strip()
        if self.cliente_existe(email_limpo):
            raise ValueError("E-mail já cadastrado.")

        cliente = {
            "id": self._proximo_cliente_id,
            "nome": str(nome).strip(),
            "email": email_limpo,
        }
        self._proximo_cliente_id += 1
        self.clientes.append(cliente)
        return cliente

    def cliente_existe(self, email):
        if not email:
            return False
        email_normalizado = str(email).strip().lower()
        return any(
            cliente["email"].strip().lower() == email_normalizado
            for cliente in self.clientes
        )

    def listar_livros(self):
        return list(self.livros)

    def pesquisar_livros(self, titulo):
        if not titulo or not str(titulo).strip():
            return list(self.livros)
        termo = str(titulo).strip().lower()
        return [
            livro for livro in self.livros
            if termo in livro["titulo"].lower()
        ]

    def adicionar_ao_carrinho(self, livro_id, quantidade):
        try:
            livro_id = int(livro_id)
        except (ValueError, TypeError):
            raise ValueError("ID do livro inválido.")

        livro = self._buscar_livro(livro_id)
        if not livro:
            raise ValueError("Livro não encontrado.")

        if isinstance(quantidade, bool) or not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A quantidade deve ser um número inteiro maior que zero.")

        qtd_atual = self.carrinho[livro_id]["quantidade"] if livro_id in self.carrinho else 0
        if qtd_atual + quantidade > livro["estoque"]:
            raise ValueError("Quantidade solicitada supera o estoque disponível.")

        nova_quantidade = qtd_atual + quantidade
        item = {
            "livro_id": livro["id"],
            "titulo": livro["titulo"],
            "autor": livro["autor"],
            "preco": livro["preco"],
            "edicao": livro["edicao"],
            "livro": dict(livro),
            "quantidade": nova_quantidade,
            "subtotal": round(livro["preco"] * nova_quantidade, 2),
        }
        self.carrinho[livro_id] = item
        return item

    def remover_do_carrinho(self, livro_id):
        try:
            livro_id = int(livro_id)
        except (ValueError, TypeError):
            raise ValueError("ID do livro inválido.")

        if livro_id not in self.carrinho:
            raise ValueError("Livro não está no carrinho.")

        del self.carrinho[livro_id]

    def visualizar_carrinho(self):
        return {
            "itens": list(self.carrinho.values()),
            "total": self.calcular_total(),
        }

    def calcular_total(self):
        return round(
            sum(item["subtotal"] for item in self.carrinho.values()),
            2,
        )

    def adicionar_aos_desejos(self, livro_id):
        try:
            livro_id = int(livro_id)
        except (ValueError, TypeError):
            raise ValueError("ID do livro inválido.")

        livro = self._buscar_livro(livro_id)
        if not livro:
            raise ValueError("Livro não encontrado.")

        if not any(d["id"] == livro["id"] for d in self.desejos):
            self.desejos.append(livro)

        return list(self.desejos)

    def listar_desejos(self):
        return list(self.desejos)

    def finalizar_compra(self, forma_pagamento, modalidade, endereco=None, loja=None):
        if not self.carrinho:
            raise ValueError("Carrinho está vazio.")

        if not forma_pagamento:
            raise ValueError("Forma de pagamento é obrigatória.")

        fp = str(forma_pagamento).strip().lower()
        if fp not in ("pix", "cartao"):
            raise ValueError("Forma de pagamento inválida. Aceitas: 'pix' ou 'cartao'.")

        if not modalidade:
            raise ValueError("Modalidade de recebimento é obrigatória.")

        mod = str(modalidade).strip().lower()
        if mod not in ("entrega", "retirada"):
            raise ValueError("Modalidade inválida. Aceitas: 'entrega' ou 'retirada'.")

        if mod == "entrega":
            if not endereco or not str(endereco).strip():
                raise ValueError("Endereço é obrigatório para modalidade entrega.")
        elif mod == "retirada":
            if not loja or not str(loja).strip():
                raise ValueError("Loja é obrigatória para modalidade retirada.")

        # Validar estoque de todos os itens antes de confirmar
        for item in self.carrinho.values():
            livro = self._buscar_livro(item["livro_id"])
            if not livro or item["quantidade"] > livro["estoque"]:
                raise ValueError(
                    f"Estoque insuficiente para o livro '{item.get('titulo', 'Desconhecido')}'."
                )

        # Reduzir estoque
        for item in self.carrinho.values():
            livro = self._buscar_livro(item["livro_id"])
            livro["estoque"] -= item["quantidade"]

        itens_pedido = list(self.carrinho.values())
        total_pedido = self.calcular_total()

        pedido = {
            "id": self._proximo_pedido_id,
            "itens": itens_pedido,
            "total": total_pedido,
            "forma_pagamento": fp,
            "modalidade": mod,
            "status": "confirmado",
        }

        if mod == "entrega":
            pedido["endereco"] = str(endereco).strip()
        elif mod == "retirada":
            pedido["loja"] = str(loja).strip()

        self._proximo_pedido_id += 1
        self.pedidos.append(pedido)
        self.carrinho.clear()

        return pedido
