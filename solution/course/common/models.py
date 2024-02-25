"""Data for the common views"""
from config.store import CustomStore
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


class UserStore(CustomStore):
    """Store for the users."""

    model_name = "users"
    backup = [
        {
            "name": "admin",
            "password": make_password("admin"),
            "role": "admin"
        },
        {
            "name": "james",
            "password": make_password("hendrix"),
            "role": "editor"
        },
        {
            "name": "fred",
            "password": make_password("baggins"),
            "role": "user"
        },
        {
            "name": "ganesh",
            "password": make_password("the_grey"),
            "role": "user"
        }
    ]


class CustomUser(AbstractUser):
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    voted_notes = ArrayField(models.CharField(), default=list, blank=True)


class Notes(models.Model):
    
    SECTION_CHOICES = [
        ('Web Frameworks', 'Web Frameworks'),
        ('Setting up Django','Setting up Django'),
        ('URL Mapping','URL Mapping'),
    ]

    text = models.TextField()
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    

class Votes(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE, related_name='user_votes')
    votes = models.BooleanField(default=False)
    section = models.CharField(max_length=50, blank= True)
    
    class Meta:
        unique_together = ('user', 'note')

