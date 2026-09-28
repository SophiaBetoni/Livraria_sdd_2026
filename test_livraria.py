import unittest

from livraria import Livraria


class TestLivraria(unittest.TestCase):

    def setUp(self):
        livros = [
            {
                "id": 1,
                "titulo": "O Hobbit",
                "autor": "J. R. R. Tolkien",
                "preco": 59.90,
                "edicao": "Capa dura",
                "estoque": 3,
            },
            {
                "id": 2,
                "titulo": "Clean Code",
                "autor": "Robert C. Martin",
                "preco": 89.90,
                "edicao": "1ª edição",
                "estoque": 0,
            },
            {
                "id": 3,
                "titulo": "Python Fluente",
                "autor": "Luciano Ramalho",
                "preco": 119.90,
                "edicao": "2ª edição",
                "estoque": 5,
            },
        ]

        self.livraria = Livraria(livros)

    def test_cadastrar_cliente(self):
        cliente = self.livraria.cadastrar_cliente(
            "Ana Silva",
            "ana@email.com",
        )

        self.assertEqual(cliente["nome"], "Ana Silva")
        self.assertTrue(
            self.livraria.cliente_existe("ANA@EMAIL.COM")
        )

    def test_impedir_email_duplicado(self):
        self.livraria.cadastrar_cliente(
            "Ana",
            "ana@email.com",
        )

        with self.assertRaises(ValueError):
            self.livraria.cadastrar_cliente(
                "Outra Ana",
                "ANA@EMAIL.COM",
            )

    def test_listar_livros_com_detalhes(self):
        livros = self.livraria.listar_livros()

        self.assertEqual(len(livros), 3)
        self.assertIn("preco", livros[0])
        self.assertIn("edicao", livros[0])
        self.assertIn("estoque", livros[0])

    def test_pesquisar_titulo_ignorando_maiusculas(self):
        resultado = self.livraria.pesquisar_livros("hob")

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "O Hobbit")

    def test_adicionar_livro_ao_carrinho(self):
        item = self.livraria.adicionar_ao_carrinho(1, 2)

        self.assertEqual(item["quantidade"], 2)
        self.assertAlmostEqual(
            item["subtotal"],
            119.80,
            places=2,
        )

    def test_acumular_quantidade_do_mesmo_livro(self):
        self.livraria.adicionar_ao_carrinho(1, 1)
        item = self.livraria.adicionar_ao_carrinho(1, 2)

        self.assertEqual(item["quantidade"], 3)

    def test_impedir_quantidade_maior_que_estoque(self):
        with self.assertRaises(ValueError):
            self.livraria.adicionar_ao_carrinho(1, 4)

    def test_remover_livro_do_carrinho(self):
        self.livraria.adicionar_ao_carrinho(1, 1)
        self.livraria.remover_do_carrinho(1)

        carrinho = self.livraria.visualizar_carrinho()

        self.assertEqual(carrinho["itens"], [])

    def test_calcular_total(self):
        self.livraria.adicionar_ao_carrinho(1, 2)
        self.livraria.adicionar_ao_carrinho(3, 1)

        self.assertAlmostEqual(
            self.livraria.calcular_total(),
            239.70,
            places=2,
        )

    def test_lista_de_desejos_sem_repeticao(self):
        self.livraria.adicionar_aos_desejos(3)
        self.livraria.adicionar_aos_desejos(3)

        desejos = self.livraria.listar_desejos()

        self.assertEqual(len(desejos), 1)

    def test_finalizar_pix_com_retirada(self):
        self.livraria.adicionar_ao_carrinho(1, 2)

        pedido = self.livraria.finalizar_compra(
            forma_pagamento="pix",
            modalidade="retirada",
            loja="Loja Centro",
        )

        self.assertEqual(pedido["status"], "confirmado")
        self.assertEqual(
            pedido["forma_pagamento"],
            "pix",
        )
        self.assertEqual(
            pedido["modalidade"],
            "retirada",
        )

        livro = self.livraria.pesquisar_livros("O Hobbit")[0]

        self.assertEqual(livro["estoque"], 1)
        self.assertEqual(
            self.livraria.visualizar_carrinho()["itens"],
            [],
        )

    def test_entrega_exige_endereco(self):
        self.livraria.adicionar_ao_carrinho(3, 1)

        with self.assertRaises(ValueError):
            self.livraria.finalizar_compra(
                forma_pagamento="cartao",
                modalidade="entrega",
            )

    def test_finalizar_cartao_com_entrega(self):
        self.livraria.adicionar_ao_carrinho(3, 1)

        pedido = self.livraria.finalizar_compra(
            forma_pagamento="cartao",
            modalidade="entrega",
            endereco="Rua das Flores, 100",
        )

        self.assertEqual(
            pedido["status"],
            "confirmado",
        )
        self.assertEqual(
            pedido["endereco"],
            "Rua das Flores, 100",
        )


if __name__ == "__main__":
    unittest.main()