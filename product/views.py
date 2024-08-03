from django.shortcuts import render, redirect
from .models import Productone
from django.views.generic import UpdateView
from .forms import ProductForm

def product(request):
    prod = Productone.objects.all()
    return render(request, 'product/product.html', {'prod': prod})


def productupdate(request):
    return render(request, 'product/updateproduct.html')


def productupdate(request):

    formname=''
    formweight=''
    # formprice=''

    if request.method == 'POST':
        Productform = ProductForm(request.POST)
        if Productform.is_valid():
            formname=Productform.cleaned_data.get('name')
            formweight=Productform.cleaned_data.get('weigth_product')
            # formprice=Productform.cleaned_data.get('pricekg')

        per = Productone.objects.filter(name=formname)[0]
        per.weigth_product += int(formweight)
        per.save()
        # per.pricekg = formprice

        return redirect('product')

    else:
        Productform = ProductForm()
    
    return render(request, 'product/updateproduct.html', {'name': formname, 'weigth_product': formweight, 'Productform': Productform})

# class ProductUpdateView(UpdateView):
#     model = Productone
#     template_name = 'food/updatefood.html'

#     fields = ['name', 'weigth_product', 'pricekg']

