from abc import ABC

from rest_framework import serializers
from .models import RecipeCategory, ProductCategory, Product, Recipe, Ingredient, SimpleRecipe, IngredientWithName, \
    MRecipe


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


class IngredientWithNameSerializers(serializers.Serializer):
    name = serializers.CharField()
    count = serializers.IntegerField()

class MRecipeSerializers(serializers.Serializer):
    category = serializers.CharField()
    name = serializers.CharField()
    img = serializers.CharField()
    protein = serializers.FloatField()
    fat = serializers.FloatField()
    carbohydrate = serializers.FloatField()
    kkal = serializers.FloatField()
    kbju = serializers.FloatField()
    description = serializers.CharField()
    ingredients = serializers.JSONField()

class SimpleRecipeSerializers(serializers.Serializer):
    category = serializers.CharField()
    recipe = serializers.CharField()
# ingredients = serializers.ListField(name=serializers.CharField, count=serializers.IntegerField())
# ingredients = serializers.ListField(child=IngredientWitNameSerializers(many=True))


# class IngredientWitNameSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = IngredientWithName
#         fields = "__all__"
#
#
# class MRecipeSerializers(serializers.ModelSerializer):
#     # ingredients = IngredientWitNameSerializers(many=True, read_only=True)
#     class Meta:
#         model = MRecipe
#         fields = "__all__"
#         # fields = ["category", "name", "ingredients"]
