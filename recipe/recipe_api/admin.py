from django.contrib import admin
from recipe_api import models


admin.site.register(models.UserProfile)
admin.site.register(models.RecipeModel)
admin.site.register(models.FollowingsModel)
# Register your models here.
