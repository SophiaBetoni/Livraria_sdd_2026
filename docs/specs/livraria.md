# Especificação — Aplicativo da Livraria

## 1. Objetivo

Desenvolver uma aplicação web de livraria que permita cadastrar clientes, consultar livros, pesquisar por título, gerenciar o carrinho, criar uma lista de desejos e finalizar pedidos.

A especificação deste documento é a fonte única de verdade do projeto.

## 2. Tecnologias

- Python
- Flask
- HTML
- CSS
- JavaScript
- unittest
- Armazenamento em memória

## 3. Escopo do protótipo

A aplicação deve permitir:

1. Cadastrar clientes.
2. Visualizar o catálogo.
3. Pesquisar livros pelo título.
4. Visualizar título, autor, preço, edição e estoque.
5. Adicionar livros ao carrinho.
6. Remover livros do carrinho.
7. Calcular o total da compra.
8. Adicionar livros à lista de desejos.
9. Finalizar compras via Pix ou cartão.
10. Escolher entrega em casa ou retirada na loja.
11. Confirmar o pedido.
12. Atualizar o estoque após a compra.

## 4. Fora do escopo

Este protótipo não deve implementar:

- Pagamentos bancários reais.
- Banco de dados.
- Autenticação com senha.
- Chat com atendente.
- Notificações reais.
- Cashback.
- Clube de benefícios.
- Recomendações automáticas.
- Integrações com transportadoras.

## 5. Modelos

### 5.1 Livro

Um livro possui:

- `id`: número inteiro único.
- `titulo`: texto.
- `autor`: texto.
- `preco`: número decimal.
- `edicao`: texto.
- `estoque`: número inteiro maior ou igual a zero.

### 5.2 Cliente

Um cliente possui:

- `id`: número inteiro único.
- `nome`: texto obrigatório.
- `email`: texto obrigatório e único.

### 5.3 Item do carrinho

Um item do carrinho possui:

- Dados do livro.
- Quantidade escolhida.
- Subtotal calculado pelo preço multiplicado pela quantidade.

### 5.4 Pedido

Um pedido possui:

- `id`: número inteiro único.
- Lista de itens.
- Valor total.
- Forma de pagamento.
- Modalidade de recebimento.
- Endereço ou loja de retirada.
- Status `confirmado`.

## 6. Regras de negócio

- RN01: o nome e o e-mail são obrigatórios no cadastro.
- RN02: dois clientes não podem utilizar o mesmo e-mail.
- RN03: a pesquisa deve ignorar letras maiúsculas e minúsculas.
- RN04: a pesquisa deve aceitar uma parte do título.
- RN05: somente livros existentes podem ser adicionados ao carrinho.
- RN06: a quantidade adicionada deve ser um número inteiro maior que zero.
- RN07: a quantidade no carrinho não pode superar o estoque do livro.
- RN08: adicionar novamente o mesmo livro deve acumular a quantidade.
- RN09: o total da compra é a soma dos subtotais dos itens.
- RN10: a lista de desejos não deve conter o mesmo livro repetido.
- RN11: as formas de pagamento aceitas são `pix` e `cartao`.
- RN12: as modalidades de recebimento aceitas são `entrega` e `retirada`.
- RN13: a modalidade `entrega` exige um endereço.
- RN14: a modalidade `retirada` exige o nome de uma loja.
- RN15: não é possível finalizar uma compra com o carrinho vazio.
- RN16: depois da confirmação do pedido, o estoque deve ser reduzido.
- RN17: depois da confirmação do pedido, o carrinho deve ser esvaziado.
- RN18: o pagamento deve ser apenas uma simulação.

## 7. Interface pública de livraria.py

A classe principal deve se chamar `Livraria` e fornecer os seguintes métodos:

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

Violações das regras de negócio devem gerar `ValueError` com uma mensagem compreensível.

## 8. Rotas Flask

A aplicação deve disponibilizar as seguintes rotas:

- `GET /`: apresenta a página principal.
- `GET /api/livros`: lista os livros.
- `GET /api/livros?q=texto`: pesquisa livros pelo título.
- `POST /api/clientes`: cadastra um cliente.
- `GET /api/carrinho`: consulta o carrinho.
- `POST /api/carrinho`: adiciona um item ao carrinho.
- `DELETE /api/carrinho/<livro_id>`: remove um item do carrinho.
- `GET /api/desejos`: consulta a lista de desejos.
- `POST /api/desejos/<livro_id>`: adiciona um livro à lista de desejos.
- `POST /api/pedidos`: finaliza uma compra.

Erros relacionados às regras de negócio devem ser devolvidos como JSON com status HTTP 400.

## 9. User Stories e critérios de aceite

### US01 — Cadastro de cliente

Como cliente, quero realizar meu cadastro para fazer compras de livros.

```gherkin
Cenário: Cadastrar cliente com dados válidos
  Dado que informei um nome e um e-mail ainda não utilizado
  Quando realizar o cadastro
  Então o cliente deve ser cadastrado com um identificador
```

```gherkin
Cenário: Impedir e-mail duplicado
  Dado que já existe um cliente com determinado e-mail
  Quando outro cadastro utilizar o mesmo e-mail
  Então o sistema deve informar que o e-mail já está cadastrado
```

### US02 — Visualização do catálogo

Como cliente, quero visualizar o catálogo para conhecer os livros disponíveis.

```gherkin
Cenário: Visualizar o catálogo
  Dado que existem livros cadastrados
  Quando acessar o catálogo
  Então devo visualizar o título, autor, preço, edição e estoque de cada livro
```

### US03 — Pesquisa de livros

Como cliente, quero pesquisar livros pelo título para encontrá-los rapidamente.

```gherkin
Cenário: Pesquisar por parte do título
  Dado que existe o livro "O Hobbit"
  Quando pesquisar por "hob"
  Então o livro "O Hobbit" deve ser apresentado
```

### US04 — Adição ao carrinho

Como cliente, quero adicionar livros ao carrinho para comprá-los.

```gherkin
Cenário: Adicionar um livro disponível ao carrinho
  Dado que o livro possui estoque suficiente
  Quando adicionar duas unidades ao carrinho
  Então o carrinho deve apresentar duas unidades e o subtotal correspondente
```

```gherkin
Cenário: Acumular a quantidade de um livro
  Dado que já existe uma unidade do livro no carrinho
  Quando adicionar mais duas unidades do mesmo livro
  Então o carrinho deve apresentar três unidades do livro
```

### US05 — Remoção do carrinho

Como cliente, quero remover livros do carrinho para alterar minha compra.

```gherkin
Cenário: Remover um livro do carrinho
  Dado que um livro está no carrinho
  Quando remover o livro
  Então ele não deve mais aparecer no carrinho
```

### US06 — Consulta de estoque

Como cliente, quero visualizar a disponibilidade do livro para decidir minha compra.

```gherkin
Cenário: Impedir quantidade maior que o estoque
  Dado que o livro possui três unidades em estoque
  Quando tentar adicionar quatro unidades ao carrinho
  Então o sistema deve informar que o estoque é insuficiente
```

### US07 — Lista de desejos

Como cliente, quero criar uma lista de desejos para guardar livros que pretendo comprar.

```gherkin
Cenário: Adicionar um livro à lista de desejos
  Dado que o livro existe
  Quando adicioná-lo à lista de desejos
  Então o livro deve aparecer uma única vez na lista
```

### US08 — Pagamento via Pix

Como cliente, quero realizar o pagamento via Pix para finalizar minha compra.

```gherkin
Cenário: Finalizar um pedido com Pix e retirada na loja
  Dado que existem livros no carrinho
  Quando escolher pagamento "pix", modalidade "retirada" e informar uma loja
  Então o pedido deve ser confirmado
  E o estoque deve ser reduzido
  E o carrinho deve ser esvaziado
```

### US09 — Pagamento com cartão

Como cliente, quero realizar o pagamento com cartão para finalizar minha compra.

```gherkin
Cenário: Finalizar um pedido com cartão e entrega em casa
  Dado que existem livros no carrinho
  Quando escolher pagamento "cartao", modalidade "entrega" e informar o endereço
  Então o pedido deve ser confirmado
```

### US10 — Entrega em casa

Como cliente, quero escolher a entrega em casa para receber os livros.

```gherkin
Cenário: Exigir o endereço para entrega
  Dado que escolhi a modalidade de entrega em casa
  Quando tentar finalizar o pedido sem informar um endereço
  Então o sistema deve impedir a finalização
  E deve informar que o endereço é obrigatório
```

### US11 — Retirada na loja

Como cliente, quero comprar pelo aplicativo e retirar o pedido na loja.

```gherkin
Cenário: Exigir a loja para retirada
  Dado que escolhi a modalidade de retirada
  Quando tentar finalizar o pedido sem informar uma loja
  Então o sistema deve impedir a finalização
  E deve informar que a loja é obrigatória
```

### US12 — Confirmação do pedido

Como cliente, quero confirmar o pedido para concluir minha compra.

```gherkin
Cenário: Impedir a finalização de um carrinho vazio
  Dado que não existem livros no carrinho
  Quando tentar finalizar a compra
  Então o sistema deve impedir a finalização
  E deve informar que o carrinho está vazio
```

```gherkin
Cenário: Confirmar um pedido válido
  Dado que existem livros disponíveis no carrinho
  E uma forma de pagamento válida foi escolhida
  E os dados da modalidade de recebimento foram informados
  Quando finalizar a compra
  Então o pedido deve receber o status "confirmado"
  E deve possuir um identificador
  E deve apresentar os itens e o valor total
```