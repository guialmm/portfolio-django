# Portfolio Django

Portfólio pessoal construído com **Django 5**, inspirado no design do [Prof. Christopher Lima](https://chrislima.github.io/profchrislima/) — dark theme, accent azul, glassmorphism nav.

## Stack

- **Backend:** Django 5, Python 3.12
- **Frontend:** Django Templates + CSS customizado (sem framework CSS externo)
- **Banco:** SQLite (dev) / PostgreSQL (prod)
- **Static files:** Whitenoise
- **Fontes:** Inter Tight + JetBrains Mono

## Estrutura

```
portfolio-django/
├── apps/
│   ├── portfolio/       # projetos, skills, contato
│   └── blog/            # posts técnicos
├── core/                # settings, urls raiz
├── static/
│   ├── css/styles.css
│   └── js/main.js
├── templates/
│   ├── base.html
│   ├── partials/navbar.html
│   └── portfolio/home.html
├── manage.py
└── requirements.txt
```

## Rodando localmente

```bash
# 1. Criar e ativar venv
python3 -m venv .venv
source .venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar variáveis (copiar e editar)
cp .env.example .env

# 4. Aplicar migrations e criar superusuário
python manage.py migrate
python manage.py createsuperuser

# 5. Subir servidor
python manage.py runserver
```

Acesse `http://localhost:8000` para o site e `http://localhost:8000/admin/` para gerenciar conteúdo.

## Features

- **Seções:** Hero, Projetos, Skills, Contato
- **Blog** técnico com posts publicáveis
- **Django Admin** para gerenciar projetos, skills e mensagens sem tocar no código
- **Dark/Light theme** com toggle e persistência via localStorage
- **Contact form** que salva mensagens no banco

## Deploy

O projeto está pronto para deploy em [Railway](https://railway.app) ou [Render](https://render.com):
- Configure `DATABASE_URL` para PostgreSQL
- Defina `DEBUG=False` e `SECRET_KEY` real no `.env`
- `python manage.py collectstatic` antes de subir
