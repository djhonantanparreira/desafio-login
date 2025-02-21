from django import forms
from django.contrib.auth.models import User
import re

class RegistrationForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100, required=True)
    email = forms.EmailField(label="E-mail", required=True)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput, required=True)
    confirmar_senha = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput, required=True)

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        # Validação: apenas letras (e espaços)
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', nome):
            raise forms.ValidationError("O nome deve conter apenas letras.")
        return nome

    def clean_senha(self):
        senha = self.cleaned_data.get('senha')
        # Validação: >=8 caracteres, 1 maiúscula, 1 número, 1 caractere especial
        if (len(senha) < 8 or
            not re.search(r'[A-Z]', senha) or
            not re.search(r'\d', senha) or
            not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)):
            raise forms.ValidationError(
                "A senha deve ter no mínimo 8 caracteres, 1 letra maiúscula, 1 número e 1 caractere especial."
            )
        return senha

    def clean(self):
        """
        Verificação final: senhas coincidem?
        """
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', "As senhas não conferem.")


class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", required=True)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput, required=True)
