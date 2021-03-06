# Generated by Django 3.1.6 on 2021-02-08 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_api', '0002_auto_20210208_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=5000)),
                ('directions', models.CharField(max_length=5000)),
                ('ingredients', models.CharField(max_length=5000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FollowingsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('follower', 'followed')},
            },
        ),
    ]
