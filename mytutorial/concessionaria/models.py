from django.db import models

# Create your models here.
class Carro(models.Model):
	chassi = models.CharField(max_length=17)
	nome_do_veiculo = models.CharField(max_length=20)
	cor = models.CharField(max_length=20)
	portas = models.CharField(max_length=2)