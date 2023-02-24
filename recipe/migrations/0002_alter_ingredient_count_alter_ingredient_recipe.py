# Generated by Django 4.1.5 on 2023-02-22 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reciperr', to='recipe.recipe'),
        ),
    ]
