# Generated by Django 4.1.5 on 2023-02-18 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0019_recipe_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
