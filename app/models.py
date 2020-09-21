from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.

# Manager for User Profile
class UserProfileManager(BaseUserManager):

    """Create a new user profile"""
    def create_user(self, email, name, password):
        
        if not email:
            raise ValueError('User must have an email address')
        
        # Make the other half part of email '@gmail.com' lowercse
        email = self.normalize_email(email)

        # Assign the new user into UserProfileManager
        user = self.model(email=email, name=name)

        # Set an encrypted hashed password
        user.set_password(password)

        # Save the user in this Database
        user.save(using=self._db)

        return user
    
    """Create and save a new superuser with given details"""
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# User Profile model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email

# User Profile Feed model
class ProfileFeedItem(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
