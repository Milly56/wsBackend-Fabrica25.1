# Consumindo uma API de Filmes

Este projeto consome a API do OMDb para buscar exclusivamente filmes da franquia Harry Potter. Para realizar as consultas, a API Key é necessária e as pesquisas devem ser feitas em inglês.

## 📌 Tecnologias Utilizadas

- *Python* (3.x)
- *Django* (Framework web)
- *PostgreSQL* (Banco de dados relacional)
- *Requests* (Para consumo da API externa)

## 🚀 Configuração do Ambiente

### 1️⃣ Criar Conta no OMDb

Acesse [OMDb API](https://www.omdbapi.com/) e registre-se para obter a chave de API que será enviada por e-mail.

### 2️⃣ Clonar o Repositório

git clone https://github.com/Milly56/wsBackend-Fabrica25.1.git

cd wsBackend-Fabrica25.1


### 3️⃣ Criar e Ativar Ambiente Virtual

*Linux:*
python3 -m venv venv
source venv/bin/activate


*Windows:*
python -m venv venv
venv\Scripts\activate


### 4️⃣ Instalar Dependências

pip install -r requirements.txt


### 5️⃣ Configurar Banco de Dados PostgreSQL

Edite o arquivo de configuração do banco de dados e defina as credenciais corretas:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bd',  
        'USER': 'postgres',       
        'PASSWORD': 'postgres',    
        'HOST': 'localhost',     
        'PORT': '5432',   
    }
}


### 6️⃣ Configurar a Chave da API no views.py

No arquivo views.py, altere a variável chave para a sua API Key:

python
chave = "[youkey]"


### 7️⃣ Aplicar Migrações do Banco de Dados


python manage.py makemigrations

python manage.py migrate


### 8️⃣ Criar um Superusuário


python manage.py createsuperuser


### 9️⃣ Executar o Servidor

python manage.py runserver


## 📌 Funcionalidades

- 🔍 Buscar filmes da franquia Harry Potter
- 👥 Criar usuários
- 🎬 Criar e gerenciar filmes
- ❌ Atualizar e deletar usuários e filmes

## 🌐 Endpoints Disponíveis

- GET http://127.0.0.1:8000/api/search → Busca por filmes de Harry Potter.
- POST http://127.0.0.1:8000/usuarios/ → Criação de usuários e filmes.
- GET/PUT/DELETE http://127.0.0.1:8000/usuarios/{id} → Gerenciamento de usuários.
- GET/PUT/DELETE http://127.0.0.1:8000/filmes/{id} → Gerenciamento de filmes.

## 🛠 Possíveis Erros e Soluções

### 🚨 requests.exceptions.ConnectionError
*Solução:* Verifique sua conexão com a internet e se a API OMDb está online.

### 🚨 django.db.utils.OperationalError: FATAL: password authentication failed
*Solução:* Confirme que as credenciais do PostgreSQL estão corretas no arquivo de configuração.

### 🚨 KeyError: 'YOUKEY'
*Solução:* Certifique-se de ter atualizado corretamente a chave da API em views.py.

## 📜 Licença

Este projeto é de uso livre para fins educacionais e pessoais.

---
Feito com ❤️ por Jamilly