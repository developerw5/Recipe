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


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    count = models.IntegerField()

    def __str__(self):
        return self.product.name + " "  + str(self.count)


class Recipe(models.Model):
    category = models.ForeignKey(RecipeCategory, models.CASCADE, related_name="category")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to)
    description = models.TextField()
    ingredient = models.ManyToManyField(Ingredient)

    # favorite = models.BooleanField()
    # my_recipe = models.BooleanField()


    def __str__(self):
        return self.name
