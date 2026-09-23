# Atividade Flask

Projeto desenvolvido como atividade prática utilizando **Python, Flask e SQLite**.

A aplicação permite cadastrar, visualizar, editar e excluir conteúdos através de uma interface web, utilizando Flask para o desenvolvimento da aplicação e SQLite para armazenamento dos dados.

---

## Objetivo

O objetivo deste projeto é aplicar na prática conceitos de desenvolvimento web com Python, incluindo:

- Criação de aplicações com Flask;
- Criação e utilização de rotas;
- Utilização de templates HTML com Jinja;
- Integração com banco de dados SQLite;
- Manipulação de dados;
- Organização de arquivos estáticos;
- Operações básicas de CRUD.

---

## Tecnologias utilizadas

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Jinja

---

## Funcionalidades

A aplicação possui as seguintes funcionalidades:

- Listagem de conteúdos cadastrados;
- Visualização individual de conteúdos;
- Cadastro de novos conteúdos;
- Edição de conteúdos existentes;
- Exclusão lógica de conteúdos;
- Página Sobre;
- Página de Contatos.

---

## CRUD

O projeto implementa as principais operações de um CRUD:

| Operação | Função |
| --- | --- |
| Create | Cadastrar um novo conteúdo |
| Read | Listar e visualizar conteúdos |
| Update | Editar conteúdos existentes |
| Delete | Desativar conteúdos |

Na exclusão, o conteúdo não é removido fisicamente do banco de dados.

O campo `c_status` é alterado de:

```text
on
```

para:

```text
off
```

Dessa forma, o registro permanece armazenado no banco, mas deixa de ser exibido na aplicação.

---

## Estrutura do projeto

```text
atividade_flask/
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── img/
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   ├── _base.html
│   ├── about.html
│   ├── contacts.html
│   ├── edit.html
│   ├── index.html
│   ├── new.html
│   └── view.html
│
├── .gitignore
├── app.py
├── database.db
├── database.sql
├── README.md
├── requirements.txt
└── setupdb.py
```

> A pasta `.venv` não é enviada para o repositório porque está configurada no `.gitignore`.

---

## Banco de dados

O projeto utiliza **SQLite**.

A tabela principal utilizada pela aplicação é `content`.

Ela armazena informações como:

- ID do conteúdo;
- Título;
- Texto;
- Data de criação;
- Status.

O arquivo:

```text
database.sql
```

contém os comandos SQL utilizados para criar a estrutura inicial do banco.

O arquivo:

```text
setupdb.py
```

é utilizado para executar o script SQL e criar o banco de dados.

---

## Como executar o projeto

### 1. Criar o ambiente virtual

No Windows:

```bash
python -m venv .venv
```

### 2. Ativar o ambiente virtual

```bash
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o banco de dados

Caso seja necessário recriar o banco:

```bash
python setupdb.py
```

### 5. Executar a aplicação

```bash
python app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

---

## Rotas principais

| Rota | Descrição |
| --- | --- |
| `/` | Página inicial |
| `/new` | Cadastro de conteúdo |
| `/view/<id>` | Visualização de conteúdo |
| `/edit/<id>` | Edição de conteúdo |
| `/delete/<id>` | Exclusão lógica |
| `/about` | Informações sobre o projeto |
| `/contacts` | Página de contatos |

---

## Autor

**Vitor Assis**

Projeto desenvolvido para fins acadêmicos e de aprendizado em desenvolvimento web com Python, Flask e SQLite.