# Generated by Django 4.1.5 on 2023-02-12 11:39

from django.db import migrations, models
import recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0012_alter_recipecategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipecategory',
            name='image',
            field=models.ImageField(upload_to=recipe.models.upload_to),
        ),
    ]
