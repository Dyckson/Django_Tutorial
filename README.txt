- Ambiente virtual(venv) =>  ----\\ python -m venv myvenv \\----
- Criar arquivo nomeado de ----\\ requirements.txt \\---- que contem o texto ---\\ Django~=2.2.4 \\---
- Executar o comando ----\\ pip install -r requirements.txt \\----

- Criar projeto ----\\ django-admin.exe startproject nome do projeto \\----

- Mudar configura��es(settings.py) do projeto, como a TIME ZONE e LANGUAGE CODE

- Criar banco de dados ----\\ python manage.py migrate \\----

- Para manter tudo arrumado, vamos criar uma aplica��o separada dentro do nosso projeto, com o comando 
  ----\\ python manage.py startapp nome da aplica��o \\----
- Adicionar ao arquivo mytutotial/settings.py => INSTALLED_APPS a nossa aplica��o criada cujo nome � 'concessionaria'