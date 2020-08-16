from django.db import models
from django.utils.timezone import datetime, timedelta
import django.utils.timezone
from django.conf import settings
from django_countries.fields import CountryField

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin,
)

from django.db.models.signals import post_save
from django.dispatch import receiver
# from pydub import AudioSegment
# from pydub.playback import play
import urllib
import stripe



stripe.api_key=settings.STRIPE_SECRET_KEY
# Create your models here.


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free.
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, *args, **kwargs):
        """Create and return a `User` with an email, username and password."""
        password = kwargs.get('password', '')
        email = kwargs.get('email', '')
        del kwargs['email']
        del kwargs['password']
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # Each `User` needs a human-readable unique identifier that we can use to
    # represent the `User` in the UI. We want to index this column in the
    # database to improve lookup performance.
    first_name = models.CharField(db_index=True, max_length=255, unique=False)

    last_name = models.CharField(db_index=True, max_length=255, unique=False)
    
    username = models.CharField(db_index=True, max_length=255, unique=False,null=True,blank=True)
    
    email = models.EmailField(db_index=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_client=models.BooleanField(' Check the checkbox alongside to signup as Client',default=False)
    is_writer=models.BooleanField(' Check the checkbox alongside to signup as Writer',default=False)
    is_administrator=models.BooleanField(' Check the checkbox alongside to signup as an Administrator',default=False)
    # is_superuser=models.BooleanField(default=True)
    is_staff = models.BooleanField('staff status',default=False)
    date_of_birth = models.DateTimeField(null=True,blank=True,default=django.utils.timezone.now)
    phone=models.CharField(max_length=200,null=True,blank=True)
    additional_phone=models.CharField(max_length=200,null=True,blank=True)
    first_discipline=models.CharField(max_length=200,null=True,blank=True)
    second_discipline=models.CharField(max_length=200,null=True,blank=True)
    third_discipline=models.CharField(max_length=200,null=True,blank=True)
    fourth_discipline=models.CharField(max_length=200,null=True,blank=True)
    fifth_discipline=models.CharField(max_length=200,null=True,blank=True)
    academic_degree=models.CharField(max_length=200,null=True,blank=True)
    time_zone=models.CharField(max_length=200,null=True,blank=True)
    night_calls=models.BooleanField(default=False,null=True,blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return str(self.username) 

    @property
    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.first_name


class Client(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    

class Writer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    username=models.CharField(max_length=255,null=True,blank=True)
    first_name=models.CharField(max_length=500,null=True,blank=True)
    password=models.CharField(max_length=1024,null=True,blank=True)
    last_name=models.CharField(max_length=500,null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    additional_phone=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    first_discipline=models.CharField(max_length=200,null=True,blank=True)
    second_discipline=models.CharField(max_length=200,null=True,blank=True)
    third_discipline=models.CharField(max_length=200,null=True,blank=True)
    fourth_discipline=models.CharField(max_length=200,null=True,blank=True)
    fifth_discipline=models.CharField(max_length=200,null=True,blank=True)
    academic_degree=models.CharField(max_length=200,null=True,blank=True)
    time_zone=models.CharField(max_length=200,null=True,blank=True)
    night_calls=models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.first_name

class Adminstration(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)


class Notification(models.Model):
    title=models.CharField(max_length=256)
    message=models.TextField()
    viewed=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    assignment=models.ForeignKey('assignments.Assignment',on_delete=models.CASCADE,null=True,blank=True)
    payment=models.ForeignKey('payments.Order',on_delete=models.CASCADE,null=True,blank=True)

@receiver(post_save,sender=User)
def create_welcome_message(sender,instance,**kwargs):
    if kwargs['created']:
        Notification.objects.create(
            user=instance,
            title='Welcome to Elite Homework Master',
            message='A new user has clocked in',
        )
        