from django.contrib import admin
from .models import User,Notification
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(User)
admin.site.register(Notification)
# admin.site.register(Group)