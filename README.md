# Desafio Login - Fidelity Pesquisas Cadastrais

Este projeto é a **2ª Etapa do Processo Seletivo** para a vaga de Desenvolvedor Back-End Estagiário na Fidelity Pesquisas Cadastrais.  
O objetivo é criar uma aplicação Django que possibilite **login**, **cadastro de usuários** e **redirecionamento** para um menu, atendendo a requisitos específicos de validação.

---

## Sumário

- [Descrição do Desafio](#descrição-do-desafio)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Requisitos Atendidos](#requisitos-atendidos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Desafios Enfrentados](#desafios-enfrentados)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Descrição do Desafio

Conforme as orientações recebidas:

- Criar uma tela de **Login** que valida se o usuário está no banco de dados e se a senha está correta.  
- Criar uma tela de **Registrar** que valida nome, e-mail, senha e confirmação de senha com regras específicas.  
- Permitir que o usuário acesse uma tela de **Menu** apenas após fazer login.  
- Seguir as mensagens de erro e validações pedidas no PDF do desafio.  
- Utilizar Django 4.x e um banco de dados relacional (SQLite, por padrão).  
- Incluir um README explicando o passo a passo.

---

## Tecnologias Utilizadas

- **Python 3.9+** (ou a versão instalada em seu sistema)
- **Django 4.2+**
- **Bootstrap 5** (para estilização simples via CDN)
- **SQLite** (banco de dados padrão do Django)

---

## Requisitos Atendidos

1. **Tela de Login**  
   - Campos de e-mail e senha (não aceitam vazio).  
   - Mensagens de erro: “E-mail inexistente”, “Senha inválida”, etc.  
   - Redirecionamento para “Menu” em caso de sucesso.  
   - Botão “Registrar” direciona para tela de registro.

2. **Tela de Registrar**  
   - Campos: nome, e-mail, senha, confirmar senha.  
   - Validações: nome só com letras, e-mail com “@”, senha >=8 caracteres, 1 maiúscula, 1 número, 1 caractere especial, confirmação igual.  
   - Opção de visualizar senhas via checkbox.  
   - Botão “Registrar” (envia form) e “Cancelar” (volta ao login).

3. **Tela de Menu**  
   - Acessível apenas se logado (usando `@login_required`).  
   - Exibe mensagem simples de boas-vindas.

4. **Extras**  
   - Utilização do `messages` do Django para feedback ao usuário.  
   - Configuração de `LOGIN_URL` para redirecionamento automático ao login se o usuário tentar acessar “Menu” sem estar autenticado.

---

## Estrutura do Projeto

```
desafio_login/
├── desafio_login/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── menu.html
│   ├── migrations/
│       └── __init__.py
├── db.sqlite3
├── manage.py
└── README.md
```

---

## Como Executar

1. **Clonar o Repositório** (ou baixar o ZIP):
   ```bash
   git clone https://github.com/djhonantanparreira/desafio-login.git
   cd desafio-login
   ```

2. **Criar e Ativar o Ambiente Virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Instalar as Dependências**:
   ```bash
   pip install django
   ```

4. **Fazer Migrações** para criar o banco:
   ```bash
   python manage.py migrate
   ```

5. **Executar o Servidor de Desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

6. **Acessar no Navegador**:
   - `http://127.0.0.1:8000/` para a tela Home.
   - `http://127.0.0.1:8000/login/` para a tela de Login.
   - `http://127.0.0.1:8000/signup/` para a tela de Registrar.
   - `http://127.0.0.1:8000/menu/` para a tela de Menu (precisa estar logado).

---

## Desafios Enfrentados

- **Validações de Senha**: Implementar regex para garantir 8 caracteres, 1 maiúscula, 1 número e 1 caractere especial.
- **Mensagens de Erro**: Exibir mensagens específicas para e-mail inexistente, senha inválida, etc.  
- **Visualizar Senha**: Incluir JavaScript para exibir/ocultar campos de senha e confirmar senha.  
- **Integração com Bootstrap**: Garantir que o layout fique simples e funcional.  
- **@login_required**: Ajustar `LOGIN_URL` no `settings.py` para redirecionar automaticamente quando o usuário não estiver logado.

---

## Licença

Este projeto foi desenvolvido para fins de avaliação técnica e não possui uma licença específica. Sinta-se livre para usar como base em estudos ou outros testes técnicos.

---