# Generated by Django 4.1.5 on 2023-02-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_rename_images_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipecategory',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
