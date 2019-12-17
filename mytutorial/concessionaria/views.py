from django.shortcuts import render
from .models import Carro

# Create your views here.
def post_list(request):
	carros = Carro.objects.all()
	return render(request, 'concessionaria/post_list.html', {'carros': carros})