from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("name", "email", "subject", "body")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Seu nome", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "seu@email.com", "autocomplete": "email"}),
            "subject": forms.TextInput(attrs={"placeholder": "Assunto"}),
            "body": forms.Textarea(attrs={"placeholder": "Sua mensagem...", "rows": 6}),
        }
        labels = {
            "name": "Nome",
            "email": "E-mail",
            "subject": "Assunto",
            "body": "Mensagem",
        }
