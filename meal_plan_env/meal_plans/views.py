from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """The home page for meal_planner"""
    return render(request, 'meal_plans/index.html')
