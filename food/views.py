from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Food, Recipe, Productone
from django.views.generic import UpdateView
from django.db.models import Sum
from .forms import FoodForm, RecipeForm

def food(request):
    eda = Food.objects.all()
    edafood = Recipe.objects.all()

    for i in range(Food.objects.all().count()):
        a = Food.objects.all()[i]
        b = Recipe.objects.filter(name=a)
        s = 0
        for q in b:
            c = Productone.objects.filter(name = q.ingredient_name)
            for k in c:
                s = s + k.pricekg * q.need
        a.price = round(s, 2)
        a.save()

    return render(request, 'food/food.html', {'eda': eda, 'edafood': edafood})


def foodupdate(request):

    submitbutton = request.POST.get('submit')

    formname=''
    formcount=''

    if request.method == 'POST':
        Foodform = FoodForm(request.POST)
        Recipeform = RecipeForm(request.POST)
        if Recipeform.is_valid():
            formname=Recipeform.cleaned_data.get('name')

        if Foodform.is_valid():
            formcount=Foodform.cleaned_data.get('countfood')

        per = Food.objects.filter(name=formname)[0]
        per.time_relise += int(formcount)
        per.save()

        if (int(formcount) > 0):
            per1 = Recipe.objects.filter(name=formname)
            for q in per1:
                per2 = Productone.objects.filter(name = q.ingredient_name)[0]
                per2.weigth_product = per2.weigth_product - (q.need * int(formcount))
                round(per2.weigth_product, 2)
                per2.save()

        return redirect('food')

    else:
        Foodform = FoodForm()
        Recipeform = RecipeForm()


    return render(request, 'food/updatefood.html', {'name': formname, 'count': formcount, 'Foodform': Foodform, 'Recipeform': Recipeform, 'submitbutton': submitbutton})

# def index(request):
#     submitbutton = request.POST.get('submit')

#     form = RecipeForm()
#     formfood = FoodForm()

#     data = {
#         'form': form,
#         'formfood': formfood
#     }

#     name = ''
#     count = ''

#     Recipeform = RecipeForm(request.POST or None)
#     if Recipeform.is_valid():
#         name = Recipeform.cleaned_data.get('name')

#     context = {'Recipeform': Recipeform, 'name': name, 'count': count, 'submitbutton': submitbutton}

#     return render(request, 'food/updatefood.html', context, data)


    # for i in range(Food.objects.all()[0].ingredient_one.all().count()):
    #     per = Productone.objects.filter(name=Food.objects.all()[0].ingredient_one.all()[i].product.name)[0]
    #     per.weigth_product -= Food.objects.all()[0].ingredient_one.all()[0].weight
    #     per.save()


# class FoodView(APIView):
#     def get(self, request):
#         articles = Food.objects.all()
#         return Response({"articles": articles})

#     def __str__(self):
#         return self.name


# class FoodUpdateView(UpdateView):
#     model = Food
#     template_name = 'food/updatefood.html'

#     fields = ['name', 'time_relise', 'weigth', 'price']
