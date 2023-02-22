from rest_framework import serializers
from .models import RecipeCategory, ProductCategory, Product, Recipe, Ingredient


class RecipeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = "__all__"


class ProductCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


    class IngredientSerializers(serializers.ModelSerializer):
        class Meta:
            model = Ingredient
            fields = "__all__"
