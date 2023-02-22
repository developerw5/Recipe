from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import RecipeCategory, ProductCategory, Recipe, Product, Ingredient
# from .serializers import RecipeSerializers, RecipeCategorySerializers, IngredientSerializers, ProductSerializers, \
#     ProductCategorySerializers


# class RecipeCategoryViewSet(viewsets.ModelViewSet):
#     queryset = RecipeCategory.objects.all()
# serializer_class = RecipeSerizalizer

# class FoodRecipe():
#     def __init__(self, recipe,kkal, protein, uglevod, fat):
#         recipe = recipe
#         kkal = kkal
#         protein = protein
#         uglevod = uglevod
#         fat = fat
#
# class FoodRecipeAPIVIEW(APIView):
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             # recipes = Recipe.objects.all()
#             # return Response({"food_recipe": recipes.values()})
#             return Response({"error": "not found  pk null"})
#
#         try:
#             ingredients = Ingredient.objects.get()
#             recipes = Product.objects.filter(category_id=pk)
#             return Response({"food_recipe": recipes.values()})
#         except:
#             return Response({"error": "except"})


class RecipeCategoryAPIView(APIView):

    def get(self, request):
        print(request)
        recipes = RecipeCategory.objects.all()

        print(recipes)
        print(type(recipes))
        print(recipes.values())

        return Response({'categories': recipes.values()})


class ProductCategoryApiView(APIView):

    def get(self, request):
        products = ProductCategory.objects.all()

        return Response({'products_category': products.values()})


class ProductApiView(APIView):

    # def get(self, request):
    #     products = Product.objects.all()
    #
    #     return Response({'products': products.values()})

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            recipes = Recipe.objects.all()
            return Response({"products": recipes.values()})
            # return Response({"error": "not found"})

        try:
            recipes = Product.objects.filter(category_id=pk)
            return Response({"products": recipes.values()})
        except:
            return Response({"error": "except"})


class IngredientApiView(APIView):

    def get(self, request):
        ingredients = Ingredient.objects.all()
        print(ingredients.values())
        return Response({'ingredients': ingredients.values()})


class RecipeApiView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            # recipes = Recipe.objects.all()
            # return Response({"recipes": recipes.values()})
            return Response({"error": "not found"})

        try:
            recipes = Recipe.objects.filter(category_id=pk)
            ingredients = recipes.ingredient.all()
            print(ingredients)
            print(recipes.values())
            print(recipes.values()[0])
            return Response({"recipes": recipes.values()})
        except:
            return Response({"error": "except"})
