from django.db import models
from io import BytesIO
import sys
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class RecipeCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to)

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((300, 300))

        # after modifications, save it to the output
        im.save(output, format='png', quality=80)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(RecipeCategory, self).save()
    # def save(self, *args, **kwargs):
    #     new_image = self.reduce_image_size(self.image)
    #     self.profile_pic = new_image
    #     super().save(*args, **kwargs)
    #
    # def reduce_image_size(self, profile_pic):
    #     print(profile_pic)
    #     img = Image.open(profile_pic)
    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'png', quality=50)
    #     new_image = File(thumb_io, name=profile_pic.name)
    #     return new_image
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product",null=True)
    recipe = models.ForeignKey(Recipe, models.CASCADE, null=True)
    count = models.FloatField(default=0)

    def __str__(self):
        return self.product.name






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
