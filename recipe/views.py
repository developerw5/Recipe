from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import RecipeCategory, ProductCategory, Recipe, Product, Ingredient, SimpleRecipe, MRecipe, IngredientWithName
from .serializers import RecipeSerializers, RecipeCategorySerializers, IngredientSerializers, ProductSerializers, \
    ProductCategorySerializers, SimpleRecipeSerializers, MRecipeSerializers, IngredientWithNameSerializers


class RecipeCategoryViewsSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = RecipeCategory.objects.all()

    serializer_class = RecipeCategorySerializers


class ProductCategoryViewsSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ProductCategory.objects.all()

    serializer_class = ProductCategorySerializers


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()

    serializer_class = ProductSerializers


class IngredientViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()

    serializer_class = IngredientSerializers


class RecipeViewSet(viewsets.ViewSet):

    def list(self, request):
        recipes = Recipe.objects.all()
        ingredients = Ingredient.objects.all()

        result_recipes = []
        for recipe in recipes.values():
            # print(recipe)
            # print(type(recipe))
            ingredients_list = Ingredient.objects.filter(recipe_id=recipe["id"]).values()
            print(ingredients_list)
            modified_ingredients_list = []
            # for i in ingredients_list:
                #ingredients_with_name = Product.objects.filter(product_id=i["product_id"])[0].name,i["count"].values()
            #     print(ingredients_with_name)
                # modified_ingredients_list.append(ingredients_with_name)
            # print("asda")
            # print(ingredients_list)
            # print("asdas")
            # print("as" + IngredientWitNameSerializers(ingredients_list, many=True))
            # result_recipes.append(
            #     MRecipe(
            #         category="",
            #         name="asd",
            #         img="af",
            #         kkal=14.4,
            #         protein=11.2,
            #         carbohydrate=55.4,
            #         fat=4.4,
            #         kbju=44.4,
            #         description="",
            #         ingredients={"ingredients": IngredientSerializers(modified_ingredients_list, many=True).data}
            #     )
            # )

        # print(recipes.values())
        # print(ingredients.values())
        # print(result_recipes)

        # return Response({"recipes": MRecipeSerializers(result_recipes, many=True).data})
        return Response({"recipes", "asdda"})

    def retrieve(self, request, pk=None):
        pass


class SimpleRecipeViewSet(viewsets.ViewSet):
    def list(self, request):
        categories = RecipeCategory.objects.all()
        recipes = Recipe.objects.all()
        firstCategories = categories.values()[0]
        firstRecipes = recipes.values()[0]

        simpleRecipe = SimpleRecipe("asd", "werew")

        return Response({"simple": SimpleRecipeSerializers(simpleRecipe).data})

#
# class SearchApiView(APIView):
#
#     def get(self, request):
#         return Response({'ingredients': "asdasd"})
#
#     # def post(self, request):
#     #     return Response({'ingredients': "asdasd"})
#
#
# class RecipeApiView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             recipes = Recipe.objects.all()
#             return Response({"recipes": recipes.values()})
#             # return Response({"error": "not found"})
#
#         try:
#             recipe = Recipe.objects.filter(category_id=pk)
#             ingredients = Ingredient.objects.filter(recipe_id=recipe[0].pk)
#             print(ingredients.values())
#             print(recipe.values())
#
#             ingredients_with_names = []
#             for i in ingredients.values():
#                 ingredients_with_name = IngredientWithName(Product.objects.filter(pk=i["product_id"])[0].name,
#                                                            i["count"])
#                 ingredients_with_names.append(ingredients_with_name)
#             return Response({"recipes": recipe.values(), "ingredients": ingredients.values()})
#
#         except:
#             return Response({"error": "except"})

# def post(self, request):


# class IngredientWithName:
#     def __init__(self, name, count):
#         name = name
#         count = count

# class IngredientApiView(APIView):
#
#     def get(self, request):
#         ingredients = Ingredient.objects.all()
#         print(ingredients.values())
#         return Response({'ingredients': ingredients.values()})


# class RecipeCategoryAPIView(APIView):
#
#     def get(self, request):
#         print(request)
#         recipes = RecipeCategory.objects.all()
#
#         print(recipes)
#         print(type(recipes))
#         print(recipes.values())
#
#         return Response({'categories': recipes.values()})


# class ProductCategoryApiView(APIView):
#
#     def get(self, request):
#         products = ProductCategory.objects.all()
#         return Response({'products_category': products.values()})
#

# class ProductApiView(APIView):
#
#     # def get(self, request):
#     #     products = Product.objects.all()
#     #
#     #     return Response({'products': products.values()})
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             product = Product.objects.all()
#             return Response({"products": product.values()})
#             # return Response({"error": "not found"})
#
#         try:
#             product = Product.objects.filter(category_id=pk)
#             return Response({"products": product.values()})
#         except:
#             return Response({"error": "except"})
