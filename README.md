# UserDemoAPI

Esta é uma API RESTful escalável e reutilizável construída com FastAPI para autenticação e gerenciamento de usuários. Ela suporta registro, login, visualização, atualização e exclusão de perfis de usuário, utilizando JWT para autenticação e SQLite como banco de dados padrão (facilmente adaptável a outros bancos via SQLAlchemy).

## Funcionalidades

- **Registro de Usuário**: Cria um novo usuário com e-mail, senha e nome completo (opcional).
- **Login de Usuário**: Autentica usuários e emite um token JWT.
- **Gerenciamento de Perfil**: Visualiza, atualiza ou exclui o perfil do usuário autenticado.
- **Autenticação Segura**: Usa bcrypt para hash de senhas e JWT para autenticação baseada em tokens.
- **Estrutura Modular**: Organizada para escalabilidade e reutilização em outros projetos.

## Estrutura do Projeto

```
project/
├── app/
│   ├── __init__.py
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── core/                 # Configurações, segurança e conexão com banco de dados
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   ├── models/               # Modelos SQLAlchemy
│   │   └── user.py
│   ├── schemas/              # Esquemas Pydantic para validação
│   │   └── user.py
│   ├── services/             # Lógica de negócios
│   │   └── user.py
│   ├── routes/               # Rotas da API
│   │   └── user.py
│   └── dependencies/         # Dependências de autenticação
│       └── auth.py
├── requirements.txt          # Dependências do projeto
└── README.md                # Este arquivo
```

## Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)
- (Opcional) Ambiente virtual

## Instalação

1. Clone o repositório:

   ```bash
   git clone <url-do-repositório>
   cd projeto
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Gere uma chave secreta segura para o JWT:
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```
   Copie a chave gerada e substitua o valor de `SECRET_KEY` no arquivo `app/core/config.py`.

## Executando a Aplicação

1. Inicie o servidor FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```
2. Acesse a documentação interativa da API em:
   ```
   http://localhost:8000/docs
   ```

## Endpoints da API

- **POST /api/v1/users/register**: Registra um novo usuário.
- **POST /api/v1/users/login**: Autentica um usuário e retorna um token JWT.
- **GET /api/v1/users/me**: Visualiza o perfil do usuário autenticado.
- **GET /api/v1/users/{user_id}**: Visualiza um usuário por ID (somente o próprio usuário).
- **PUT /api/v1/users/{user_id}**: Atualiza os dados do usuário (somente o próprio usuário).
- **DELETE /api/v1/users/{user_id}**: Exclui o usuário (somente o próprio usuário).

## Exemplo de Uso

### Registro de Usuário

```bash
curl -X POST "http://localhost:8000/api/v1/users/register" \
-H "Content-Type: application/json" \
-d '{"email": "user@example.com", "password": "senha123", "full_name": "Nome Completo"}'
```

### Login

```bash
curl -X POST "http://localhost:8000/api/v1/users/login" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=user@example.com&password=senha123"
```

### Visualizar Perfil (com token JWT)

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
-H "Authorization: Bearer <seu-token-jwt>"
```

## Configuração para Produção

- **Banco de Dados**: Substitua o SQLite por um banco mais robusto (ex.: PostgreSQL) alterando a `DATABASE_URL` em `app/core/config.py`.
- **Chave Secreta**: Use uma chave segura para `SECRET_KEY` e armazene-a em um arquivo `.env`.
- **CORS**: Ajuste as configurações de CORS em `app/main.py` para permitir apenas origens confiáveis
