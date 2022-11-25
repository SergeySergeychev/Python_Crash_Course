from django.contrib import admin
from meal_plans.models import MealPlan, DayOftheWeek
# Register your models here.
admin.site.register(MealPlan)
admin.site.register(DayOftheWeek)
