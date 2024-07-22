# Django API REST - CRUD de Usuários

Este projeto é uma API RESTful para gerenciamento de usuários, construída com Django e Django REST Framework. A API permite realizar operações CRUD (Create, Read, Update, Delete) para usuários.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework

## Instalação

1. **Clone o repositório**
    ```sh
    git clone https://github.com/leiriele/apiDjango.git
    cd seu-repositorio
    ```
2. **Crie e Ative o Ambiente Virtual**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instale as Dependências**

    ```bash
    pip install -r requirements.txt
    ```

4. **Realize as Migrações do Banco de Dados**

    ```bash
    python manage.py migrate
    ```

5. **Crie um Superusuário para acessar o Admin**

    ```bash
    python manage.py createsuperuser
    ```

6. **Inicie o Servidor**

    ```bash
    python manage.py runserver
    ```

## Estrutura da API

### Endpoints

- **Listar Todos os Usuários**
    - **Método:** `GET`
    - **URL:** `/api/users/`
    - **Descrição:** Retorna uma lista de todos os usuários.
    - **Resposta:** Uma lista JSON de usuários.

- **Obter Usuário por Nickname**
    - **Método:** `GET`
    - **URL:** `/api/users/<nick>/`
    - **Descrição:** Retorna os detalhes do usuário com o nickname especificado.
    - **Parâmetro URL:** `nick` (o nickname do usuário)
    - **Resposta:** Detalhes do usuário em formato JSON.

- **Criar Novo Usuário**
    - **Método:** `POST`
    - **URL:** `/api/user/`
    - **Descrição:** Cria um novo usuário com os dados fornecidos.
    - **Corpo da Requisição:** Dados do usuário (nickname, nome, e-mail, idade) em formato JSON.
    - **Resposta:** Detalhes do novo usuário em formato JSON.

- **Atualizar Usuário**
    - **Método:** `PUT`
    - **URL:** `/api/user/<nick>/`
    - **Descrição:** Atualiza o usuário com o nickname especificado.
    - **Parâmetro URL:** `nick` (o nickname do usuário)
    - **Corpo da Requisição:** Dados do usuário a serem atualizados em formato JSON.
    - **Resposta:** Detalhes do usuário atualizado em formato JSON.

- **Excluir Usuário**
    - **Método:** `DELETE`
    - **URL:** `/api/user/<nick>/`
    - **Descrição:** Exclui o usuário com o nickname especificado.
    - **Parâmetro URL:** `nick` (o nickname do usuário)
    - **Resposta:** Status da operação.

### Exemplo de Requisições

- **Listar Todos os Usuários:**

    ```bash
    curl -X GET http://127.0.0.1:8000/api/users/
    ```

- **Obter Usuário por Nickname:**

    ```bash
    curl -X GET http://127.0.0.1:8000/api/users/Leiriele/
    ```

- **Criar Novo Usuário:**

    ```bash
    curl -X POST http://127.0.0.1:8000/api/user/ \
    -H "Content-Type: application/json" \
    -d '{"user_nickname": "Leiriele", "user_name": "Leiriele Santos", "user_email": "leiriele@example.com", "user_age": 30}'
    ```

- **Atualizar Usuário:**

    ```bash
    curl -X PUT http://127.0.0.1:8000/api/user/Leiriele/ \
    -H "Content-Type: application/json" \
    -d '{"user_name": "Leiriele Silva", "user_age": 31}'
    ```

- **Excluir Usuário:**

    ```bash
    curl -X DELETE http://127.0.0.1:8000/api/user/Leiriele/
    ```

## Admin do Django

Você pode acessar o painel de administração do Django para gerenciar usuários e outras configurações através do seguinte URL:

- **Admin:** `/admin/`
- **Crie um superusuário:** `python manage.py createsuperuser` para acessar o painel de administração.

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para fazer um fork e enviar pull requests. Siga as melhores práticas de desenvolvimento e escreva testes para garantir que suas alterações funcionem corretamente.



