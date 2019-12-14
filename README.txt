- Ambiente virtual(venv) =>  ----\\ python -m venv myvenv \\----
- Criar arquivo nomeado de ----\\ requirements.txt \\---- que contem o texto ---\\ Django~=2.2.4 \\---
- Executar o comando ----\\ pip install -r requirements.txt \\----

- Criar projeto ----\\ django-admin.exe startproject nome do projeto \\----

- Mudar configurações(settings.py) do projeto, como a TIME ZONE e LANGUAGE CODE

- Criar banco de dados ----\\ python manage.py migrate \\----

- Para manter tudo arrumado, vamos criar uma aplicação separada dentro do nosso projeto, com o comando 
  ----\\ python manage.py startapp nome da aplicação \\----
- Adicionar ao arquivo mytutotial/settings.py => INSTALLED_APPS a nossa aplicação criada cujo nome é 'concessionaria'

- Agora podemos escolher os campos que aparecerão na nossa aplicação // Vamos até model.py na nossa aplicação e criaremos
  a ----\\ classe Carro(models.Model): \\----

- O último passo é adicionar nosso novo modelo(Carro) com o comando ----\\ python manage.py makemigrations concessionaria \\----
- Adicionar ele ao banco de dados com ----\\ python manage.py migrate concessionaria \\----