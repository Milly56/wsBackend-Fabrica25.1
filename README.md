<h1>Consumindo uma Api de Filmes</h1>
<h2>Que tem Api key e apareci só as pesquisas de filmes de Harry Potter</h2>
<h3>Pré requisito:</h3>
<h4>ter uma conta no https://www.omdbapi.com/ </h4>
<h4>que vai ser enviado via email a chave </h4>
<h4>após isso modifique no arquivo views.py do app,modique a variável chave</h4>
<h3>Primeiros Passos:</h3>
<h4>git clone https://github.com/Milly56/wsBackend-Fabrica25.1.git</h4>
<h4>após a instalação,entre no arquivo e crie um ambiente virtual</h4>
<h4>Python3 -m venv venv - Linux</h4>
<h4>Python -m venv venv - Windows</h4>
<h4>logo após isso,habilitar o ambiente virtual</h4>
<h4>. venv/bin/activate - Linux</h4>
<h4>venv/scripts/activate - Windows</h4>
<h4>agora é hora de instalar as depedências do projeto:</h4>
<h4>pip install -r requirements.txt</h4>
<h4>Conecte com o postgress com as credencias:</h4>
<p> 'NAME': 'bd',  
    'USER': 'postgres',       
    'PASSWORD': 'postgres',    
    'HOST': 'localhost',     
    'PORT': '5432',   </p>
    <h4>após isso,rode os sequintes comandos:</h4>
    <h4>python manage.py makemigrations</h4>
    <h4>python manage.py migrate</h4>
    <h4>e crie um superusuário com o sequinte comando:</h4>
    <h4>python manage.py createsuperuser</h4>
    <h4>e rode a aplicação com o sequinte comando:</h4>
    <h4>python manage.py runserver</h4>
<h4>caminhos:</h4>
<h4>http://127.0.0.1:8000/api/search</h4>
<h5>para buscar de filmes de Harry Potter</h5>
<h4>http://127.0.0.1:8000/usuarios/</h4>
<h5>para criação de usuários e filmes</h5>
<h4>após criar coloque o id encima,exemplo:</h4>
<h4>http://127.0.0.1:8000/usuarios/usuarios/{id}</h4>
<h4>que irá para outra página para deletação e atualização de usuários</h4>
<h4>também tem isso no filmes</h4>

