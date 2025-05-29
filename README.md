# API RESTful para Clube de Assinatura

Este projeto é uma API RESTful simples para gerenciar um clube de assinatura, construída com Python e Flask. Utiliza dicionários em memória para simular um banco de dados, ideal para fins de estudo e prototipagem rápida.

## Entidades Principais

A API gerencia as seguintes entidades:

* **Membros:** Usuários que assinam o clube.
* **Assinaturas:** Planos de assinatura associados aos membros.
* **Produtos:** Itens que são enviados nas caixas de assinatura.
* **Envios:** Registros de caixas enviadas para os membros, contendo produtos.

## Requisitos

* Python 3.8+
* pip (gerenciador de pacotes do Python)

## Configuração do Ambiente

Siga os passos abaixo para configurar e rodar a API em sua máquina local:

1.  **Clone este repositório** (ou descompacte o arquivo ZIP) para o seu computador.
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd clube_assinatura_api
    ```

2.  **Crie e ative um ambiente virtual:**
    É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

    * **No macOS / Linux:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    * **No Windows:**
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```
    Você deve ver `(.venv)` no início da linha de comando do seu terminal, indicando que o ambiente virtual está ativo.

3.  **Instale as dependências:**
    Com o ambiente virtual ativado, instale as bibliotecas necessárias usando o `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Executando a API

Para iniciar o servidor da API:

1.  Certifique-se de que seu ambiente virtual está ativo e você está na pasta raiz do projeto (`clube_assinatura_api`).
2.  Execute o arquivo `app.py`:

    ```bash
    python app/app.py
    ```
    A API estará rodando em `http://127.0.0.1:5000/`.

## Endpoints da API

A API expõe os seguintes endpoints:

### Membros

* `GET /membros`
    * Lista todos os membros.
* `GET /membros/<id>`
    * Obtém detalhes de um membro específico.
* `POST /membros`
    * Cria um novo membro.
    * **Exemplo de corpo da requisição (JSON):**
        ```json
        {
            "nome": "Fulano de Tal",
            "email": "fulano@email.com"
        }
        ```
* `PUT /membros/<id>`
    * Atualiza um membro existente.
    * **Exemplo de corpo da requisição (JSON):**
        ```json
        {
            "email": "novo.email@email.com"
        }
        ```
* `DELETE /membros/<id>`
    * Deleta um membro.

### Assinaturas

* `GET /assinaturas`
    * Lista todas as assinaturas.
* `GET /assinaturas/<id>`
    * Obtém detalhes de uma assinatura específica.
* `POST /assinaturas`
    * Cria uma nova assinatura para um membro.
    * **Exemplo de corpo da requisição (JSON):**
        ```json
        {
            "membro_id": "1",
            "plano": "mensal",
            "data_inicio": "2024-01-01",
            "ativa": true
        }
        ```
* `PUT /assinaturas/<id>`
    * Atualiza uma assinatura.
* `DELETE /assinaturas/<id>`
    * Cancela/deleta uma assinatura.

### Produtos

* `GET /produtos`
    * Lista todos os produtos.
* `GET /produtos/<id>`
    * Obtém detalhes de um produto específico.
* `POST /produtos`
    * Cria um novo produto.
    * **Exemplo de corpo da requisição (JSON):**
        ```json
        {
            "nome": "Livro de Receitas",
            "descricao": "Livro com receitas exclusivas do clube",
            "preco": 75.50
        }
        ```
* `PUT /produtos/<id>`
    * Atualiza um produto.
* `DELETE /produtos/<id>`
    * Deleta um produto.

### Envios

* `GET /envios`
    * Lista todos os envios.
* `GET /envios/<id>`
    * Obtém detalhes de um envio específico.
* `POST /envios`
    * Registra um novo envio (caixa do mês).
    * **Exemplo de corpo da requisição (JSON):**
        ```json
        {
            "membro_id": "1",
            "data_envio": "2024-05-30",
            "itens": [
                {"produto_id": "1", "quantidade": 1},
                {"produto_id": "2", "quantidade": 1}
            ],
            "status": "pendente"
        }
        ```
* `PUT /envios/<id>`
    * Atualiza um envio.
* `DELETE /envios/<id>`
    * Deleta um envio.

### Envios por Membro

* `GET /membros/<id>/envios`
    * Lista todos os envios de um membro específico.

## Testando a API

Você pode usar ferramentas como `curl` (via terminal), Postman, Insomnia ou Thunder Client (extensão do VS Code) para testar os endpoints.

**Exemplo com `curl` (para criar um membro):**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"nome": "Novo Membro", "email": "novo.membro@example.com"}' [http://127.0.0.1:5000/membros](http://127.0.0.1:5000/membros)