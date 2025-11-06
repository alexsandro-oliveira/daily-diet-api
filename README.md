# 🍎 Daily Diet API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green?style=for-the-badge&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-latest-orange?style=for-the-badge&logo=mysql)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

**API REST para controle de dieta diária desenvolvida com Flask**

[Sobre](#-sobre) •
[Funcionalidades](#-funcionalidades) •
[Tecnologias](#-tecnologias) •
[Instalação](#-instalação) •
[Uso](#-uso) •
[Endpoints](#-endpoints-da-api) •
[Estrutura](#-estrutura-do-projeto)

</div>

---

## 📖 Sobre

A **Daily Diet API** é um projeto de estudos desenvolvido para aprender e praticar conceitos de desenvolvimento de APIs REST com Python e Flask. O objetivo é criar uma aplicação que permita aos usuários registrar suas refeições diárias, marcando se estão ou não dentro da dieta, além de gerenciar usuários com autenticação.

## ✨ Funcionalidades

### 👤 Gerenciamento de Usuários
- ✅ Cadastro de novos usuários com senha criptografada (bcrypt)
- ✅ Autenticação de usuários (login/logout)
- ✅ Consulta, atualização e exclusão de usuários
- ✅ Sistema de permissões (roles)
- ✅ Proteção de rotas com autenticação obrigatória

### 🍽️ Gerenciamento de Refeições
- ✅ Registro de refeições com título, descrição e horário
- ✅ Marcação de refeições dentro/fora da dieta
- ✅ Listagem de todas as refeições do usuário logado
- ✅ Consulta de refeição específica por ID
- ✅ Edição e exclusão de refeições
- ✅ Associação automática com o usuário autenticado

## 🛠️ Tecnologias

Este projeto foi desenvolvido com as seguintes tecnologias:

### Backend
- **[Python 3.12](https://www.python.org/)** - Linguagem de programação
- **[Flask 2.3.0](https://flask.palletsprojects.com/)** - Framework web minimalista
- **[Flask-SQLAlchemy 3.1.1](https://flask-sqlalchemy.palletsprojects.com/)** - ORM para integração com banco de dados
- **[Flask-Login 0.6.2](https://flask-login.readthedocs.io/)** - Gerenciamento de sessões de usuário
- **[bcrypt 5.0.0](https://github.com/pyca/bcrypt/)** - Criptografia de senhas
- **[python-dotenv 1.2.1](https://github.com/theskumar/python-dotenv)** - Gerenciamento de variáveis de ambiente

### Banco de Dados
- **[MySQL](https://www.mysql.com/)** - Sistema de gerenciamento de banco de dados relacional
- **[PyMySQL 1.1.0](https://github.com/PyMySQL/PyMySQL)** - Driver Python para MySQL
- **[Docker](https://www.docker.com/)** - Containerização do banco de dados

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

- [Python 3.12+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes Python)
- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/alexsandro-oliveira/daily-diet-api.git
cd daily-diet-api
```

### 2. Configure o ambiente virtual Python

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate

# No Windows:
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SECRET_KEY=sua_chave_secreta_super_segura_aqui
MYSQL_DATABASE_URI=mysql+pymysql://admin:admin123@localhost:3306/daily-diet
```

> 💡 **Dica:** Gere uma SECRET_KEY segura com o comando Python:
> ```bash
> python -c "import secrets; print(secrets.token_hex(32))"
> ```

### 5. Inicie o banco de dados com Docker

```bash
docker-compose up -d
```

### 6. Crie as tabelas no banco de dados

```bash
# Opção 1: Via Flask Shell
export FLASK_APP=app.py
flask shell
>>> from database import db
>>> db.create_all()
>>> exit()

# Opção 2: Via Python
python -c "from app import app; from database import db; app.app_context().push(); db.create_all(); print('Tabelas criadas com sucesso!')"
```

## 🎮 Uso

### Iniciar o servidor de desenvolvimento

```bash
python app.py
```

O servidor estará rodando em `http://localhost:5000`

### Testar a API

Você pode testar os endpoints usando ferramentas como:
- [Postman](https://www.postman.com/)
- [Insomnia](https://insomnia.rest/)
- [cURL](https://curl.se/)
- [HTTPie](https://httpie.io/)

## 📡 Endpoints da API

### 🔐 Autenticação

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/login` | Realizar login | ❌ |
| `GET` | `/logout` | Realizar logout | ✅ |

**Exemplo de Login:**
```json
POST /login
Content-Type: application/json

{
  "username": "usuario123",
  "password": "senha123"
}
```

### 👥 Usuários

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/user` | Criar novo usuário | ✅ |
| `GET` | `/user/<id>` | Buscar usuário por ID | ✅ |
| `PUT` | `/user/<id>` | Atualizar senha do usuário | ✅ |
| `DELETE` | `/user/<id>` | Deletar usuário | ✅ |

**Exemplo de Criação de Usuário:**
```json
POST /user
Content-Type: application/json
Authorization: Bearer <token>

{
  "username": "novousuario",
  "password": "senhasegura123",
  "role": "user"
}
```

### 🍽️ Refeições

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/food` | Registrar nova refeição | ✅ |
| `GET` | `/food` | Listar todas as refeições do usuário | ✅ |
| `GET` | `/food/<id>` | Buscar refeição por ID | ✅ |
| `PUT` | `/food/<id>` | Atualizar refeição | ✅ |
| `DELETE` | `/food/<id>` | Deletar refeição | ✅ |

**Exemplo de Registro de Refeição:**
```json
POST /food
Content-Type: application/json
Authorization: Bearer <token>

{
  "title": "Café da Manhã",
  "description": "Pão integral com ovos e café",
  "eated_at": "2025-11-06 08:00:00",
  "on_diet": true
}
```

**Resposta de Listagem:**
```json
GET /food

[
  {
    "title": "Café da Manhã",
    "description": "Pão integral com ovos e café",
    "eated_at": "06-11-2025 08:00:00",
    "on_diet": true
  },
  {
    "title": "Almoço",
    "description": "Arroz, feijão, frango e salada",
    "eated_at": "06-11-2025 12:30:00",
    "on_diet": true
  }
]
```

## 📁 Estrutura do Projeto

```
daily-diet-api/
├── model/
│   ├── user.py          # Model de Usuário
│   └── food.py          # Model de Refeição
├── __pycache__/         # Cache Python (não versionado)
├── app.py               # Aplicação principal e rotas
├── database.py          # Configuração do SQLAlchemy
├── docker-compose.yml   # Configuração do Docker para MySQL
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente (não versionado)
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Documentação do projeto
```

## 🗃️ Modelo de Dados

### Tabela `user`
```python
id: Integer (PK)
username: String(80) UNIQUE NOT NULL
password: String(80) NOT NULL  # Senha criptografada com bcrypt
role: String(50) NOT NULL DEFAULT 'user'
```

### Tabela `food`
```python
id: Integer (PK)
title: String(100) NOT NULL
description: Text
eated_at: DateTime NOT NULL
on_diet: Boolean NOT NULL
user_id: Integer (FK -> user.id)
```

## 🔧 Configuração do Banco de Dados

O projeto utiliza MySQL rodando em um container Docker. As configurações estão no arquivo `docker-compose.yml`:

- **Host:** localhost
- **Porta:** 3306
- **Usuário:** admin
- **Senha:** admin123
- **Database:** daily-diet

Para acessar o MySQL diretamente:

```bash
docker exec -it <container_id> mysql -u admin -p
# Senha: admin123
```

## 🐛 Solução de Problemas Comuns

### Erro: "NameError: name 'db' is not defined" no Flask Shell

**Causa:** O objeto `db` não está disponível automaticamente no contexto do shell.

**Solução:**
```bash
# No flask shell, importe manualmente:
from database import db
from app import app

# Use o contexto da aplicação:
with app.app_context():
    db.create_all()
```

### Erro de Conexão com MySQL

**Verifique se o container está rodando:**
```bash
docker ps
```

**Reinicie o container se necessário:**
```bash
docker-compose down
docker-compose up -d
```

### Problemas com Migrações

Se precisar recriar as tabelas:
```bash
# Conecte ao MySQL
docker exec -it <container_id> mysql -u admin -p

# No MySQL:
DROP DATABASE `daily-diet`;
CREATE DATABASE `daily-diet`;
exit;

# Recrie as tabelas
python -c "from app import app; from database import db; app.app_context().push(); db.create_all()"
```

## 📚 Aprendizados

Este projeto foi desenvolvido como parte dos estudos e permitiu aprender:

- ✅ Desenvolvimento de APIs REST com Flask
- ✅ Autenticação e autorização de usuários
- ✅ Integração com banco de dados usando SQLAlchemy (ORM)
- ✅ Criptografia de senhas com bcrypt
- ✅ Uso de variáveis de ambiente para configuração
- ✅ Containerização de serviços com Docker
- ✅ Relacionamentos entre tabelas (1:N)
- ✅ Boas práticas de estruturação de projetos Flask

## 🚧 Possíveis Melhorias Futuras

- [ ] Implementar validação de dados com marshmallow
- [ ] Adicionar paginação nas listagens
- [ ] Criar sistema de métricas (sequência de dias na dieta, etc.)
- [ ] Implementar testes automatizados (pytest)
- [ ] Adicionar documentação da API com Swagger/OpenAPI
- [ ] Melhorar tratamento de erros e exceções
- [ ] Implementar JWT para autenticação stateless
- [ ] Adicionar migrations com Flask-Migrate/Alembic
- [ ] Criar endpoints de estatísticas de dieta

## 🤝 Contribuindo

Este é um projeto de estudos, mas contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Alexsandro Oliveira**

- GitHub: [@alexsandro-oliveira](https://github.com/alexsandro-oliveira)

## 🙏 Agradecimentos

- [Rocketseat](https://www.rocketseat.com.br/) - Pela excelente formação em desenvolvimento
- Comunidade Python Brasil
- Documentação oficial do Flask

---

<div align="center">

**Desenvolvido com 💜 durante os estudos na Rocketseat**

⭐ Se este projeto te ajudou, considere dar uma estrela!

</div>
