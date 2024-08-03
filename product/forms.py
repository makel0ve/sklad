from .models import Productone
from django.forms import ModelForm

class ProductForm(ModelForm):
  class Meta:
    model = Productone
    fields = ['name', 'weigth_product']