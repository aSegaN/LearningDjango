from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


# Create your views here.
# /menu
def index(request):
    pizzas = Pizza.objects.all()
    """
    pizzas_names_and_prices = [pizza.nom + ":" + str(pizza.prix) + "$" for pizza in pizzas]
    pizzas_names_str_and_prices = ", ".join(pizzas_names_and_prices)
    return HttpResponse(pizzas_names_str_and_prices)
    """
    return render(request, 'menu/index.html', {'pizzas': pizzas})


