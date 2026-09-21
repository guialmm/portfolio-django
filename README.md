# Portfolio Django

**[Demo ao vivo](https://portfolio-django-opal.vercel.app)**

Portfólio pessoal construído com **Django 5** — dark theme, CSS customizado, admin CMS e blog técnico.

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
│   ├── portfolio/       # hub, projetos, stack, contato
│   └── blog/            # lista e detalhe de posts
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

# 3. Configurar variáveis de ambiente
cp .env.example .env

# 4. Aplicar migrations
python manage.py migrate

# 5. Popular banco com dados iniciais
python manage.py loaddata apps/portfolio/fixtures/initial_data.json

# 6. Criar superusuário para o admin
python manage.py createsuperuser

# 7. Subir servidor
python manage.py runserver
```

Acesse `http://localhost:8000` para o site e `http://localhost:8000/admin/` para gerenciar conteúdo.

## Páginas

| Rota | Descrição |
|---|---|
| `/` | Hub — página inicial com links para as seções |
| `/projetos/` | Lista de projetos com filtro por categoria |
| `/projetos/<slug>/` | Detalhe de cada projeto |
| `/stack/` | Tecnologias e linguagens |
| `/blog/` | Lista de posts técnicos |
| `/blog/<slug>/` | Detalhe de um post |
| `/contato/` | Formulário de contato |
| `/admin/` | Painel de administração |

## Features

- **Hub** com cards de navegação e status "disponível para estágios"
- **Projetos** com filtro por categoria (IA, Web, CLI) e página de detalhe
- **Stack** agrupada por categoria com filtro
- **Blog** técnico com posts publicáveis via admin
- **Django Admin** para gerenciar projetos, skills e mensagens sem tocar no código
- **Dark/Light theme** com toggle persistente via localStorage
- **Reveal animations** via IntersectionObserver
- **Contact form** que salva mensagens no banco

## Deploy

Rodando na [Vercel](https://vercel.com) (function serverless via `@vercel/python`) +
[Aiven](https://aiven.io) PostgreSQL (plano free, sem cartão). Também dá pra usar
[Render](https://render.com) (`render.yaml` incluso), mais simples por rodar como
processo persistente de verdade — a Vercel não tem filesystem persistente, então
o SQLite não serve, precisa de um Postgres externo.

Variáveis de ambiente em produção:

```bash
DEBUG=False
SECRET_KEY=<chave-longa-e-aleatória>
DATABASE_URL=postgres://user:senha@host:porta/banco?sslmode=require
ALLOWED_HOSTS=seudominio.com   # opcional — já inclui .vercel.app e .onrender.com por padrão
```

Vercel: `vercel.json` + `build_files.sh` cuidam do build (instala dependências e
roda `collectstatic`); migrations e `loaddata` do fixture precisam rodar uma vez
manualmente contra o banco (não tem processo de start persistente pra rodar isso
a cada deploy, diferente do Render):

```bash
DATABASE_URL=... SECRET_KEY=... python manage.py migrate
DATABASE_URL=... SECRET_KEY=... python manage.py loaddata apps/portfolio/fixtures/initial_data.json
DATABASE_URL=... SECRET_KEY=... python manage.py createsuperuser
```

### Limitações

- Formulário de contato salva no Postgres normalmente (funciona igual em
  qualquer um dos dois hosts) — a limitação de storage efêmero é só pra
  uploads de imagem via admin (`media/`), que não persistem entre deploys
  na Vercel.
