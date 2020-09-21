from rest_framework import serializers
from app import models

# Hello Serializer
class HelloSerializer(serializers.Serializer):

    """Serializes name field for testing APIView"""
    name = serializers.CharField(max_length=10)


# User Profile Serializer
class UserProfileSerializer(serializers.ModelSerializer):

    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        # Use theses fields for creating a profile object
        fields = ('id', 'email', 'name', 'password')
        
        # Make the password inaccessible in GET request and don't show in plain text  
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    """Create and retun a new user"""
    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

# User Profile Serializer
class ProfileFeedItemSerializer(serializers.ModelSerializer):

    """Serializes a user profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        # Use theses fields for creating a profile object
        fields = ('id', 'user_profile', 'status_text', 'created_on')

        # Make the user profile read only so that unauthorized users can't make any change to other profiles  
        extra_kwargs = {
            'user_profile':{'read_only':True}
        }

