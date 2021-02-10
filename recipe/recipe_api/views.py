from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from recipe_api import models, serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from recipe_api import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers as coreSerializers




# Create your views here.

class UserLoginApiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
    

class UserProfileViewSet(viewsets.ModelViewSet):
    # renderer_classes = [JSONRenderer]

    serializer_class=serializers.UserProfileSerializer
    queryset =models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes =(permissions.UpdateOwnProfile,)
    # filter_backends=(filters.SearchFilter,)
    # search_fields=('name', 'email')

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer # this is overall model serialier including create
    queryset = models.RecipeModel.objects.all()
    for query in queryset:

        print(serializers.RecipeSerializer(query).data)
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication]  #for token athentication


    def list(self, request):
        relatedUser = list(models.FollowingsModel.objects.filter(follower = request.user).values_list('followed', flat=True))
        relatedUser.append(request.user)
        queryset = models.RecipeModel.objects.filter(created_by__in=relatedUser)
       #print(queryset) can we query set
        # output = ', '.join([q.title for q in queryset]) we can iterate on query set like this

        result = serializers.RecipeListSerializer(queryset, many=True) # if a nested representation should be a list of items, you should pass the many=True flag to the nested serialized.

        return Response({'recipes': result.data})


    def perform_create(self, serializer):  # need to create this function to set the owner
        print(serializer)
        # return
        serializer.save(created_by = self.request.user)

    def retrieve(self, request, pk=None):
        relatedUser = list(models.FollowingsModel.objects.filter(follower = request.user).values_list('followed', flat=True))
        relatedUser.append(request.user)
        queryset = models.RecipeModel.objects.get(created_by__in=relatedUser, pk=pk) # need to set pk=pk get to get single pk record
        result = serializers.RecipeSerializer(queryset) 

        return Response({'recipes': result.data})


class FollowingViewSet(viewsets.ModelViewSet):
    """This will be used for following users"""

    serializer_class = serializers.FollowingsSerializer
    queryset = models.FollowingsModel.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post', 'get']


    def list(self, request, pk=None):
        """This will return the list of followings"""

        queryset = models.FollowingsModel.objects.filter(follower=request.user)
        serializer = serializers.FollowingsSerializerList(queryset, many=True)
        return Response({'followings':serializer.data}) 