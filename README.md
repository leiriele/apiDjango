# Django API Rest 

Este é um boilerplate genérico para projetos Django API Rest. Ele implementa operações CRUD para gerenciamento de usuários.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/leiriele/apiDjango.git
    cd seu-repositorio
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

## Endpoints da API

A API oferece os seguintes endpoints para gerenciar usuários:

### Listar Usuários

- **URL**: `/api/users/`
- **Método HTTP**: `GET`
- **Descrição**: Retorna uma lista de todos os usuários.

### Criar Usuário

- **URL**: `/api/users/`
- **Método HTTP**: `POST`
- **Descrição**: Cria um novo usuário.
- **Dados do Corpo da Requisição**:
    ```json
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }
    ```

### Obter Usuário

- **URL**: `/api/users/{id}/`
- **Método HTTP**: `GET`
- **Descrição**: Retorna os detalhes de um usuário específico.

### Atualizar Usuário

- **URL**: `/api/users/{id}/`
- **Método HTTP**: `PUT`
- **Descrição**: Atualiza as informações de um usuário específico.
- **Dados do Corpo da Requisição**:
    ```json
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }
    ```

### Deletar Usuário

- **URL**: `/api/users/{id}/`
- **Método HTTP**: `DELETE`
- **Descrição**: Remove um usuário específico.

## Estrutura do Projeto


