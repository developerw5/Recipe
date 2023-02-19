from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RecipeCategory, ProductCategory,  Recipe, Product


class RecipeCategoryAPIView(APIView):

    def get(self, request):
        recipes = RecipeCategory.objects.all()

        print(recipes)
        print(type(recipes))
        print(recipes.values())

        return Response({'categories': recipes.values()})

    # def post(self, request):
    #     new_recipe_category = RecipeCategory.objects.create(
    #         name=request.data["name"],
    #         image=request.data["images"]
    #     )
    #     return Response({'post': model_to_dict(new_recipe_category)})


class ProductCategoryApiView(APIView):

    def get(self, request):
        products = ProductCategory.objects.all()

        return Response({'products_category': products.values()})


class ProductApiView(APIView):

    def get(self, request):
        products = Product.objects.all()

        return Response({'products': products.values()})


# class IngredientApiView(APIView):
#
#     def get(self, request):
#         ingredients = Ingredient.objects.all()
#
#         return Response({'ingredients': ingredients.values()})


class RecipeApiView(APIView):

    def get(self, request):
        recipes = Recipe.objects.all()

        return Response({"recipes": recipes.values()})
