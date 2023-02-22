from django.contrib import admin

# Register your models here.
from .models import RecipeCategory, Recipe, ProductCategory, Product, Ingredient

# admin.site.register(Recipe)
admin.site.register(RecipeCategory)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Ingredient)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal = ['ingredient']
