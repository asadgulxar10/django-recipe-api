# Generated by Django 3.1.6 on 2021-02-08 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_api', '0003_followingsmodel_recipemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followingsmodel',
            old_name='created_on',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='recipemodel',
            old_name='created_on',
            new_name='created_date',
        ),
    ]
