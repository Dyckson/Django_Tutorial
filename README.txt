- Ambiente virtual(venv) =>  ----\\ python -m venv myvenv \\----
- Criar arquivo nomeado de ----\\ requirements.txt \\---- que contem o texto ---\\ Django~=2.2.4 \\---
- Executar o comando ----\\ pip install -r requirements.txt \\----

- Criar projeto ----\\ django-admin.exe startproject nome do projeto \\----

- Mudar configura��es(settings.py) do projeto, como a TIME ZONE e LANGUAGE CODE

- Criar banco de dados ----\\ python manage.py migrate \\----

- Para manter tudo arrumado, vamos criar uma aplica��o separada dentro do nosso projeto, com o comando 
  ----\\ python manage.py startapp nome da aplica��o \\----
- Adicionar ao arquivo mytutotial/settings.py => INSTALLED_APPS a nossa aplica��o criada cujo nome � 'concessionaria'

- Agora podemos escolher os campos que aparecer�o na nossa aplica��o // Vamos at� model.py na nossa aplica��o e criaremos
  a ----\\ classe Carro(models.Model): \\----

- O �ltimo passo � adicionar nosso novo modelo(Carro) com o comando ----\\ python manage.py makemigrations concessionaria \\----
- Adicionar ele ao banco de dados com ----\\ python manage.py migrate concessionaria \\----

- Para observar todo o nosso progresso vamos criar um super usu�rio para acessar o admin do site 
  python manage.py createsuperuser e acessar a http://127.0.0.1:8000/admin/ no navegador

- Fazer a importa��o do .model Carro para a concessionaria/admin.py

- Uma view � o lugar onde n�s colocamos a "l�gica" da nossa aplica��o. Ela vai extrair informa��es do model que voc� criou e entreg�-las a um template

- Criando o metodo post_list e os diret�rios template/concessionaria