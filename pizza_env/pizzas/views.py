from django.shortcuts import render
from . models import Pizza, Topping

# Create your views here.
def index(request):
    """The home page for pizzas."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all available pizzas for today."""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Show a single pizza with it toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)
