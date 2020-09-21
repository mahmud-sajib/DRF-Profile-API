from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from app import serializers
from app import models
from app import permissions
# Create your views here.

# Working with APIView
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    """Returns a list of APIView features"""
    def get(self, request, format=None):

        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Similar to a traditional Django View',
            'Gives most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({ 'message':'Hello!', 'an_apiview':an_apiview })

    """Create a message with our given name"""
    def post(self, request):
        # Get the requested data
        serializer = self.serializer_class(data=request.data)

        # Check if the data is valid
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({ 'message':message })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """Handle updating an object"""
    def put(self, request, pk=None):
        return Response({ 'method':'PUT' })

    """Handle partial update of an object"""
    def patch(self, request, pk=None):
        return Response({ 'method':'PATCH' })
    
    """Handle deleting object"""
    def delete(self, request, pk=None):
        return Response({ 'method':'DELETE' })


# Working with ViewSet
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({ 'message':'Hello', 'a_viewset':a_viewset })
    
    """Create a message with our given name"""
    def create(self, request):
        # Get the requested data
        serializer = self.serializer_class(data=request.data)

        # Check if the data is valid
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({ 'message':message })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """Handle getting an object by it's id"""
    def retrieve(self, request, pk=None):
        return Response({ 'http_method':'GET' })

    """Handle updating of an object"""
    def update(self, request, pk=None):
        return Response({ 'http_method':'PUT' })

    """Handle partially updating of an object"""
    def partial_update(self, request, pk=None):
        return Response({ 'http_method':'PATCH' })
    
    """Handle removing of an object"""
    def destroy(self, request, pk=None):
        return Response({ 'http_method':'DELETE' })


# Working with User Profile Api (Handle creating and updating profiles)
class UserProfileViewSet(viewsets.ModelViewSet):
    # Specify serializer class for operation 
    serializer_class = serializers.UserProfileSerializer
    
    # Get all objects from UserProfile object 
    queryset = models.UserProfile.objects.all()

    # Add authentication & permission for users
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )

    # Add search capability on specified fields
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)


# Working with User Login Api (Handle creating user authentication tokens)
class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Working with User Profile Feed Api (Handle creating, reading and updating profile feed items)
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        # IsAuthenticatedOrReadOnly,
        IsAuthenticated
    )

    """Set the user profile to logged in user"""
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)



    




