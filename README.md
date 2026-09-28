# Livraria SDD

Aplicação web de uma livraria desenvolvida em Python e Flask utilizando a abordagem **Specification-Driven Development (SDD)**.

O projeto foi construído a partir de uma especificação formal, contendo User Stories, critérios de aceite em Gherkin, regras de negócio, tarefas de implementação e testes unitários.

## Objetivo

Permitir que clientes consultem livros, pesquisem pelo título, gerenciem um carrinho e uma lista de desejos e finalizem pedidos com diferentes formas de pagamento e recebimento.

## Funcionalidades

- Cadastro de clientes.
- Visualização do catálogo de livros.
- Pesquisa de livros pelo título.
- Consulta de preço, autor, edição e estoque.
- Adição de livros ao carrinho.
- Remoção de livros do carrinho.
- Cálculo do subtotal e do valor total.
- Validação da quantidade disponível em estoque.
- Lista de desejos sem itens repetidos.
- Pagamento simulado via Pix.
- Pagamento simulado com cartão.
- Entrega em casa.
- Retirada do pedido na loja.
- Confirmação do pedido.
- Atualização do estoque depois da compra.
- Limpeza do carrinho depois da compra.

## Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- JavaScript
- unittest
- Git e GitHub
- Gemini CLI como agente de desenvolvimento

## Metodologia SDD

A aplicação foi desenvolvida seguindo o fluxo:

1. Definição das especificações.
2. Criação das User Stories.
3. Escrita dos critérios de aceite em Gherkin.
4. Definição das regras de negócio.
5. Criação das tarefas de desenvolvimento.
6. Escrita dos testes unitários.
7. Implementação orientada pela especificação.
8. Execução e validação dos testes.
9. Teste manual da aplicação web.

A especificação é considerada a fonte única de verdade do projeto.

## Estrutura do projeto

```text
Livraria_sdd_2026/
├── docs/
│   └── specs/
│       ├── livraria.md
│       └── tasks.md
├── templates/
│   └── index.html
├── app.py
├── livraria.py
├── test_livraria.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Descrição dos arquivos

- `docs/specs/livraria.md`: especificações, User Stories, critérios de aceite e regras de negócio.
- `docs/specs/tasks.md`: tarefas utilizadas para orientar o desenvolvimento.
- `livraria.py`: regras de negócio e classe principal da livraria.
- `test_livraria.py`: testes unitários.
- `app.py`: servidor Flask e rotas da API.
- `templates/index.html`: interface web da aplicação.
- `requirements.txt`: dependências necessárias.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SophiaBetoni/Livraria_sdd_2026.git
```

### 2. Entrar na pasta

```bash
cd Livraria_sdd_2026
```

### 3. Criar o ambiente virtual

No Windows:

```powershell
py -m venv .venv
```

### 4. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```powershell
py -m pip install -r requirements.txt
```

### 6. Executar os testes

```powershell
py -m unittest -v
```

Resultado esperado:

```text
Ran 13 tests
OK
```

### 7. Executar a aplicação

```powershell
py app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

## Rotas da API

| Método | Rota | Finalidade |
|---|---|---|
| GET | `/` | Exibir a página principal |
| GET | `/api/livros` | Listar os livros |
| GET | `/api/livros?q=texto` | Pesquisar pelo título |
| POST | `/api/clientes` | Cadastrar cliente |
| GET | `/api/carrinho` | Consultar o carrinho |
| POST | `/api/carrinho` | Adicionar item ao carrinho |
| DELETE | `/api/carrinho/<livro_id>` | Remover item do carrinho |
| GET | `/api/desejos` | Consultar a lista de desejos |
| POST | `/api/desejos/<livro_id>` | Adicionar livro aos desejos |
| POST | `/api/pedidos` | Finalizar um pedido |

## Testes unitários

Os testes verificam:

- Cadastro de cliente.
- Bloqueio de e-mail duplicado.
- Listagem dos livros.
- Pesquisa sem diferenciação entre letras maiúsculas e minúsculas.
- Adição e remoção de livros do carrinho.
- Acúmulo de quantidade.
- Validação do estoque.
- Cálculo do total.
- Lista de desejos sem repetição.
- Pagamento via Pix com retirada.
- Pagamento com cartão e entrega.
- Obrigatoriedade do endereço para entrega.

## Limitações do protótipo

Esta é uma aplicação acadêmica. Por isso:

- Os dados são armazenados somente em memória.
- Os dados são apagados quando o servidor é encerrado.
- Os pagamentos são simulados.
- Não existe autenticação com senha.
- Não há integração bancária.
- Não há integração com transportadoras.
- Não há banco de dados.

## Autora

**Sophia Nishimura Betoni**

Estudante de Engenharia da Computação — Universidade Presbiteriana Mackenzie.