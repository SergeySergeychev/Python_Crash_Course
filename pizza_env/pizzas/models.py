from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Model to hold field with name of pizzas."""
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Topping(models.Model):
    """Model to hold fields as pizza and toppings."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.CharField(max_length=50)
    def __str__(self):
        return self.topping
