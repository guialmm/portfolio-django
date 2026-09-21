#!/bin/bash
# Rodado pela Vercel (build @vercel/static-build) antes do deploy: instala
# as dependências e gera os arquivos estáticos em staticfiles/, que o
# vercel.json serve direto (sem passar pela function Python do Django).
pip install --break-system-packages -r requirements.txt
python manage.py collectstatic --noinput
