from django.db import models
# Create your models here.

class MealPlan(models.Model):
    """Class to create your own meal."""
    meal= models.TextField()

    def __str__(self):
        """Reurn a string representation of the model."""
        return self.meal

class DayOftheWeek(models.Model):
    meals = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    day = models.CharField(max_length=15)

    def __str__(self):
        """Return a string representetion of provided information."""
        return self.day
