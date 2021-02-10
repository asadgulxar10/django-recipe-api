from rest_framework import serializers
from recipe_api import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
class RecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.RecipeModel
        fields = ('id', 'title', 'description', 'directions', 'ingredients', 'created_by', 'created_date')
        extra_kwargs = {
            'created_by': {
                'read_only': True,
            },
            'created_date': {
                'read_only': True,
            }
        }



class RecipeListSerializer(serializers.ModelSerializer):
    created_by = UserProfileSerializer()
    class Meta:
        model = models.RecipeModel
        fields = ('id', 'title', 'description', 'directions', 'ingredients', 'created_by', 'created_date')
        extra_kwargs = {
            'created_by': {
                'read_only': True,
            },
            'created_date': {
                'read_only': True,
            }
        }

class FollowingsSerializer(serializers.ModelSerializer):
    """This is the serializer class for following the users"""

    class Meta:
        model = models.FollowingsModel
        fields = ('id', 'followed', 'follower', 'created_date')
        extra_kwargs = {'follower':{'read_only':True}, 'created_date':{'read_only':True}}
        unique_together = ('followed','follower')

    def create(self, validated_data):
        """Custom create method of the followings"""

        following = models.FollowingsModel(
            followed = validated_data['followed']
        )
        request = self.context.get('request', None)
        following.follower = request.user
        existings = models.FollowingsModel.objects.filter(followed=following.followed, follower=following.follower)
        if len(existings) == 0:
            following.save()
            return following
        elif following.follower == following.followed:
            raise serializers.ValidationError({'message':'You Cannot follow yourself'})

        raise serializers.ValidationError({'message':'You have already followed this user.'})

class FollowingsSerializerList(serializers.ModelSerializer):
    """This will be used to return the list of followings"""
    follower = UserProfileSerializer()
    followed = UserProfileSerializer()
    class Meta:
        model = models.FollowingsModel
        fields = ('id', 'followed', 'follower', 'created_date')