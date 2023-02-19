from rest_framework import serializers
from .models import RecipeCategory


class RecipeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = "__all__"
