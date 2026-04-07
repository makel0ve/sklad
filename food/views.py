from django.shortcuts import render, redirect

from .models import Food, Recipe, Productone
from .forms import FoodForm, RecipeForm


def food(request):
    eda = Food.objects.all()
    edafood = Recipe.objects.all()

    for item in Food.objects.all():
        recipes = Recipe.objects.filter(name=item)
        total_price = 0
        for recipe in recipes:
            ingredient = Productone.objects.filter(name=recipe.ingredient_name).first()
            if ingredient:
                total_price += ingredient.pricekg * recipe.need
                
        item.price = round(total_price, 2)
        item.save()

    return render(request, 'food/food.html', {'eda': eda, 'edafood': edafood})


def foodupdate(request):
    submitbutton = request.POST.get('submit')

    formname = ''
    formcount = ''

    if request.method == 'POST':
        Foodform = FoodForm(request.POST)
        Recipeform = RecipeForm(request.POST)

        if Recipeform.is_valid():
            formname = Recipeform.cleaned_data.get('name')

        if Foodform.is_valid():
            formcount = Foodform.cleaned_data.get('countfood')

        per = Food.objects.filter(name=formname)[0]
        per.time_relise += int(formcount)
        per.save()

        if int(formcount) > 0:
            recipes = Recipe.objects.filter(name=formname)
            for recipe in recipes:
                ingredient = Productone.objects.filter(name=recipe.ingredient_name)[0]
                ingredient.weigth_product -= recipe.need * int(formcount)
                ingredient.weigth_product = round(ingredient.weigth_product, 2)
                ingredient.save()

        return redirect('food')

    else:
        Foodform = FoodForm()
        Recipeform = RecipeForm()

    return render(request, 'food/updatefood.html', {
        'name': formname,
        'count': formcount,
        'Foodform': Foodform,
        'Recipeform': Recipeform,
        'submitbutton': submitbutton,
    })