# Generated by Django 3.1.6 on 2021-02-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_api', '0004_auto_20210208_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='directions',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='ingredients',
            field=models.CharField(max_length=255),
        ),
    ]
