# Generated by Django 4.1.5 on 2023-02-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0018_remove_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipe.ingredient'),
        ),
    ]
