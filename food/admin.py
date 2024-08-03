from django.contrib import admin

from .models import Food, Recipe


class FoodIngredientAdmin(admin.TabularInline):
    model = Recipe
    extra = 0


class FoodAdmin(admin.ModelAdmin):
    inlines = [FoodIngredientAdmin, ]

    class Meta:
        model = Food


admin.site.register(Food, FoodAdmin)
admin.site.register(Recipe)