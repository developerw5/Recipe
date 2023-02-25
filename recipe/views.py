import rest_framework.request
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import RecipeCategory, ProductCategory, Recipe, Product, Ingredient, SimpleRecipe, MRecipe, \
    IngredientWithName
from .serializers import RecipeSerializers, RecipeCategorySerializers, IngredientSerializers, ProductSerializers, \
    ProductCategorySerializers, SimpleRecipeSerializers, MRecipeSerializers, IngredientWithNameSerializers
from rest_framework.decorators import action

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


# class RecipeViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Recipe.objects.all()
#     #
#     serializer_class = RecipeSerializers

class RecipeViewSet(viewsets.ViewSet):

    def calculateKBJU(self, kkal, fat, carbohydrate, protein):
        return 0

    def handle(self, recipes):
        result_recipes = []

        for recipe in recipes:
            ingredients = Ingredient.objects.filter(recipe_id=recipe["id"]).values()
            result_ingredients = []
            kkal = 0
            fat = 0
            carbohydrate = 0
            protein = 0
            for ingredient in ingredients:
                print(type(ingredient))
                product = Product.objects.filter(id=ingredient["product_id"]).values()[0]
                kkal += product["kkal"]
                protein += product["protein"]
                carbohydrate += product["carbohydrate"]
                fat += product["fat"]
                result_ingredients.append(IngredientWithName(product["name"], ingredient["count"]))

            result_recipes.append(
                MRecipe(
                    category=recipe["category_id"],
                    name=recipe["name"],
                    img=recipe["image"],
                    kkal=kkal,
                    fat=fat,
                    carbohydrate=carbohydrate,
                    protein=protein,
                    kbju=kkal*500/100,
                    description=recipe["description"],
                    ingredients=IngredientWithNameSerializers(result_ingredients, many=True).data
                )
            )
        return result_recipes

    def list(self, request):
        recipes = Recipe.objects.all().values()
        print(type(recipes))
        return Response({"recipes": MRecipeSerializers(self.handle(recipes), many=True).data})

    def retrieve(self, request, pk=None):
        print(pk)
        recipe_query_set = Recipe.objects.filter(pk=pk).values()
        print(recipe_query_set)
        recipe_dict = recipe_query_set[0]
        print(type(recipe_dict))
        print(recipe_dict)
        ingredients = Ingredient.objects.filter(recipe_id=recipe_dict["id"]).values()
        result_ingredients = []
        kkal = 0
        fat = 0
        carbohydrate = 0
        protein = 0
        for ingredient in ingredients:
            print(type(ingredient))
            product = Product.objects.filter(id=ingredient["product_id"]).values()[0]
            kkal += product["kkal"]
            protein += product["protein"]
            carbohydrate += product["carbohydrate"]
            fat += product["fat"]
            result_ingredients.append(IngredientWithName(product["name"], ingredient["count"]))

        result_recipe = MRecipe(
            category=recipe_dict["category_id"],
            name=recipe_dict["name"],
            img="media/"+recipe_dict["image"],
            kkal=kkal,
            fat=fat,
            carbohydrate=carbohydrate,
            protein=protein,
            kbju=kkal*500/100,
            description=recipe_dict["description"],
            ingredients=IngredientWithNameSerializers(result_ingredients, many=True).data
        )
        print(type(recipe_query_set))
        return Response({"recipe": MRecipeSerializers(result_recipe).data})
        # else:
        #     print("elses")
        #     return Response({"recipe": []})



class SearchApiView(APIView):

    def handle(self, recipes, product_name):
        result_recipes = []

        for recipe in recipes:
            ingredients = Ingredient.objects.filter(recipe_id=recipe["id"]).values()
            result_ingredients = []
            kkal = 0
            fat = 0
            carbohydrate = 0
            protein = 0
            have = False
            for ingredient in ingredients:
                product = Product.objects.filter(id=ingredient["product_id"]).values()[0]
                kkal += product["kkal"]
                protein += product["protein"]
                carbohydrate += product["carbohydrate"]
                fat += product["fat"]
                if product["name"] == product_name:
                    have = True
                result_ingredients.append(IngredientWithName(product["name"], ingredient["count"]))

            if have:
                result_recipes.append(
                    MRecipe(
                        category=recipe["category_id"],
                        name=recipe["name"],
                        img=recipe["image"],
                        kkal=kkal,
                        fat=fat,
                        carbohydrate=carbohydrate,
                        protein=protein,
                        kbju=kkal*500/100,
                        description=recipe["description"],
                        ingredients=IngredientWithNameSerializers(result_ingredients, many=True).data
                    )
                )
        return result_recipes

    def get(self, request):
        print(request)

        try:
            name = request.query_params["recipe"]
            print(name)
            recipes = Recipe.objects.filter(name=name).values()
            result_recipes = []

            for recipe in recipes:
                ingredients = Ingredient.objects.filter(recipe_id=recipe["id"]).values()
                result_ingredients = []
                kkal = 0
                fat = 0
                carbohydrate = 0
                protein = 0
                for ingredient in ingredients:
                    print(type(ingredient))
                    product = Product.objects.filter(id=ingredient["product_id"]).first()
                    kkal += product["kkal"]
                    protein += product["protein"]
                    carbohydrate += product["carbohydrate"]
                    fat += product["fat"]
                    result_ingredients.append(IngredientWithName(product["name"], ingredient["count"]))

                result_recipes.append(
                    MRecipe(
                        category=recipe["category_id"],
                        name=recipe["name"],
                        img=recipe["image"],
                        kkal=kkal,
                        fat=fat,
                        carbohydrate=carbohydrate,
                        protein=protein,
                        kbju=kkal*500/100,
                        description=recipe["description"],
                        ingredients=IngredientWithNameSerializers(result_ingredients, many=True).data
                    )
                )
            return Response({"recipes": MRecipeSerializers(result_recipes,many=True).data})

        except:
            print("An except occured ")

        try:
            recipes = Recipe.objects.all().values()
            name = request.query_params["product"]
            modified_recipes = self.handle(recipes, name)
            print(modified_recipes)
            return Response({"products": MRecipeSerializers(modified_recipes,many=True).data})
        except:
            print("An except occured")

        return  Response({"error": "wrong paramters"})


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
