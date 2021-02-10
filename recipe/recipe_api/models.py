from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name , password):

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=50)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

class RecipeModel(models.Model):
    """This class is the model class for recipies"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    directions = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    created_by = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    REQUIRED_FIELDS = ['title', 'description']


    def __str__(self):
        """String operator is being overridden here"""

        return self.title

class FollowingsModel(models.Model):
    """This class will hold the followings of the users"""

    id = models.AutoField(primary_key=True)
    followed = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='followed')
    follower = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='follower')
    created_date = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    class Meta:
        unique_together = ('follower', 'followed')
