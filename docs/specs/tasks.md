# Tasks do projeto

O agente deve utilizar o arquivo `docs/specs/livraria.md` como fonte única de verdade para implementar a aplicação.

## T01 — Ler a especificação e os testes

- Ler completamente o arquivo `docs/specs/livraria.md`.
- Ler completamente o arquivo `test_livraria.py`.
- Identificar as regras de negócio, os métodos e os comportamentos esperados.
- Não criar regras de negócio que não estejam definidas na especificação.
- Não modificar o arquivo `docs/specs/livraria.md`.

## T02 — Implementar o domínio da aplicação

Implementar no arquivo `livraria.py`:

- A classe principal `Livraria`.
- O armazenamento dos livros em memória.
- O cadastro de clientes.
- A validação de e-mail duplicado.
- A listagem do catálogo.
- A pesquisa de livros pelo título.
- A adição de livros ao carrinho.
- A remoção de livros do carrinho.
- O cálculo dos subtotais.
- O cálculo do total da compra.
- A lista de desejos.
- A validação do estoque.
- A finalização dos pedidos.
- A atualização do estoque depois da compra.
- A limpeza do carrinho depois da compra.

A classe `Livraria` deve fornecer os seguintes métodos:

- `cadastrar_cliente(nome, email)`
- `cliente_existe(email)`
- `listar_livros()`
- `pesquisar_livros(titulo)`
- `adicionar_ao_carrinho(livro_id, quantidade)`
- `remover_do_carrinho(livro_id)`
- `visualizar_carrinho()`
- `calcular_total()`
- `adicionar_aos_desejos(livro_id)`
- `listar_desejos()`
- `finalizar_compra(forma_pagamento, modalidade, endereco=None, loja=None)`

## T03 — Executar os testes unitários

- Executar o comando `py -m unittest -v`.
- Corrigir o arquivo `livraria.py` até todos os testes passarem.
- Não alterar os testes para esconder falhas na implementação.
- Todos os testes devem terminar com o resultado `OK`.
- Não continuar para o back-end enquanto existirem testes falhando.

## T04 — Implementar o back-end Flask

Implementar no arquivo `app.py`:

- Criar a aplicação Flask.
- Criar o catálogo inicial de livros.
- Criar uma instância da classe `Livraria`.
- Implementar a rota principal da aplicação.
- Implementar as rotas da API.
- Receber os dados enviados em formato JSON.
- Devolver as respostas em formato JSON.
- Tratar erros do tipo `ValueError`.
- Devolver status HTTP 400 para erros de regras de negócio.
- Permitir a execução da aplicação com o comando `py app.py`.

Devem ser implementadas as seguintes rotas:

- `GET /`
- `GET /api/livros`
- `GET /api/livros?q=texto`
- `POST /api/clientes`
- `GET /api/carrinho`
- `POST /api/carrinho`
- `DELETE /api/carrinho/<livro_id>`
- `GET /api/desejos`
- `POST /api/desejos/<livro_id>`
- `POST /api/pedidos`

## T05 — Implementar o front-end

Implementar no arquivo `templates/index.html`:

- Cabeçalho da livraria.
- Área para cadastro do cliente.
- Campo de pesquisa de livros.
- Catálogo organizado em cartões.
- Exibição do título do livro.
- Exibição do autor.
- Exibição do preço.
- Exibição da edição.
- Exibição da quantidade disponível em estoque.
- Campo para selecionar a quantidade.
- Botão para adicionar ao carrinho.
- Botão para adicionar à lista de desejos.
- Área para visualizar o carrinho.
- Botão para remover um livro do carrinho.
- Exibição do subtotal de cada item.
- Exibição do valor total da compra.
- Área para visualizar a lista de desejos.
- Formulário para finalizar o pedido.
- Escolha da forma de pagamento entre Pix e cartão.
- Escolha da modalidade entre entrega e retirada.
- Campo para endereço de entrega.
- Campo para informar a loja de retirada.
- Botão para confirmar o pedido.
- Mensagens de sucesso e erro.
- Interface adaptável para celular e computador.

O CSS e o JavaScript devem permanecer dentro do próprio arquivo `index.html`.

O JavaScript deve consumir as rotas Flask por meio da função `fetch`.

## T06 — Validar a aplicação

- Executar novamente o comando `py -m unittest -v`.
- Confirmar que todos os testes terminam com `OK`.
- Executar a aplicação com o comando `py app.py`.
- Acessar `http://127.0.0.1:5000`.
- Testar a pesquisa de livros.
- Testar o cadastro do cliente.
- Testar a adição e a remoção de livros do carrinho.
- Testar a lista de desejos.
- Testar a finalização com Pix e retirada.
- Testar a finalização com cartão e entrega.
- Testar as mensagens de erro.

## T07 — Revisar o código

- Não adicionar funcionalidades que estejam fora da especificação.
- Não implementar pagamentos reais.
- Não utilizar banco de dados.
- Não incluir chaves de API no código.
- Não incluir senhas ou informações pessoais no repositório.
- Manter o código organizado e compreensível para apresentação acadêmica.
- Não modificar `docs/specs/livraria.md`.
- Não modificar `test_livraria.py` para fazer testes incorretos passarem.
- Apresentar um resumo dos arquivos implementados e dos testes executados.