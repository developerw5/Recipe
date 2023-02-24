from django.db import models


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class RecipeCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to)
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    kkal = models.FloatField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(RecipeCategory, models.CASCADE, related_name="category")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING, related_name="reciperr", null=True)
    count = models.IntegerField()

    def __str__(self):
        return "Ingredient"



# class IngredientWithName(models.Model):
#     name = models.CharField()
#     count = models.IntegerField()
#
# class MRecipe(models.Model):
#     category = models.IntegerField()
#     name = models.CharField()
#     img = models.ImageField()
#     kkal = models.FloatField()
#     protein = models.FloatField()
#     carbohydrate = models.FloatField()
#     fat = models.FloatField()
#     kbju = models.FloatField()
#     description = models.CharField()


class MRecipe:
    def __init__(self, category, name, img, kkal, protein, carbohydrate, fat, kbju, description, ingredients):
        self.category = category
        self.name = name
        self.img = img
        self.kkal = kkal
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat
        self.kbju = kbju
        self.description = description
        self.ingredients = ingredients


class IngredientWithName:
    def __init__(self, name, count):
        self.name = name
        self.count = count


class SimpleRecipe:
    def __init__(self, category, recipe):
        self.category = category
        self.recipe = recipe
