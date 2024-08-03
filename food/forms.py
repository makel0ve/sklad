from .models import Food, Recipe
from django.forms import ModelForm

class FoodForm(ModelForm):
  class Meta:
    model = Food
    fields = ['countfood']

class RecipeForm(ModelForm):
  class Meta:
    model = Recipe
    fields = ['name']