from django.db import models
from django_countries.fields import CountryField
from django.contrib import messages
from django.utils import timezone
from .choices import ASSIGNMENT_LEVELS,ASSIGNMENT_TYPES
from django.conf import settings
from django.db.models import Q,Avg
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import (
    post_save,post_migrate,post_init,
    post_delete,pre_delete,pre_init,
    pre_migrate,pre_save
)
from authentication.models import User,Notification
from chat.models import ChatMessage,Thread
import subprocess
# Create your models here.
# from payments.models import Membership


class Assignment(models.Model):
    STATUS_CHOICES=[
        ('APP','Approved'),
        ('PEN','Ongoing'),
        ('COMP','Completed'),
        ('REV','Return for Revision'),
        ('BID','Accept'),
        ('PRIV','Private'),
        ('DIS', 'Disputed'),
        ('MP','Mark Paid')
    ]
    slug=models.SlugField(null=True)
    level = models.CharField(max_length=20,choices=ASSIGNMENT_LEVELS)
    types = models.CharField(max_length=20,choices=ASSIGNMENT_TYPES)
    country = CountryField()
    location=models.CharField(max_length=1024,null=True,blank=True)
    description=models.CharField(verbose_name='course_description',max_length=255,blank=True)
    document=models.FileField(upload_to='documents/',null=True)
    writer_document=models.FileField(upload_to='documents/',null=True)
    task=models.CharField(max_length=1024,null=True,blank=True)
    uploaded_at=models.DateTimeField(null=True,blank=True)
    deadline=models.DateTimeField()
    price_delta=models.IntegerField(null=True,blank=True)
    writers_deadline=models.DateTimeField(null=True,blank=True)
    support=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='client_support')
    creator=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    writer=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='assigned_writer')
    completed_date=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=23,choices=STATUS_CHOICES,null=True,blank=True,default='PRIV')
    price=models.IntegerField(null=True,blank=True)
    return_reason=models.CharField(max_length=255,null=True,blank=True)
    revise=models.BooleanField(default=False)
    viewed=models.BooleanField(default=False)
    writers_amount=models.IntegerField(null=True,blank=True)
    solution_format=models.CharField(max_length=200,null=True,blank=True)
    ip_address=models.GenericIPAddressField(unique=False,null=True,blank=True)
    more_info=models.TextField('More Information Section',max_length=1200,null=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.uploaded_at = timezone.now()
        self.modified = timezone.now()
        return super(Assignment, self).save(*args, **kwargs)
    class Meta:
        ordering=['-uploaded_at']

    @property
    def get_subtracted_price(self):
        recalculated_price=abs(self.price-self.price_delta)
        return recalculated_price

    @property
    def get_added_price(self):
        recalculated_price=abs(self.price+self.price_delta)
        return recalculated_price

    
@receiver(post_save,sender=Assignment)
def new_assignment(sender,instance,**kwargs):
    print('you have added a new assignment do you notice am a pre save method')
    if kwargs['created']:
            objects,thread = Thread.objects.get_or_new(instance.creator,instance.support)
            ChatMessage.objects.create(
                thread=objects,
                user=instance.support,
                title='A new assignment',
                notification='A new assignment called ({}) has been added by {}'.format(instance.description,instance.creator),
                assignment=instance,
            )
            
@receiver(pre_save,sender=Assignment)
def issue_quote(sender,instance,update_fields,**kwargs):
        objects,thread = Thread.objects.get_or_new(instance.creator,instance.support)
        if instance.writer:
            objects_writer,thread_writer=Thread.objects.get_or_new(instance.writer,instance.support)
        if not instance._state.adding:
            assignment=Assignment.objects.get(pk=instance.pk)
            if assignment.price != instance.price:
                ChatMessage.objects.create(
                thread=objects,
                user=instance.creator,
                title='The quote has been changed',
                notification='We have issued you  a quote of ${} for assignment ({})'.format(instance.price,instance.description),
                assignment=instance,
                )
            
            elif assignment.writer != instance.writer:
                ChatMessage.objects.create(
                thread=objects_writer,
                user=instance.creator,
                title='a writer asssigned',
                notification='the assignment ({}) has been assigned a writer {}'.format(instance.description,instance.writer),
                assignment=instance,
                )
            elif assignment.status != instance.status:
                ChatMessage.objects.create(
                thread=objects,
                user=instance.creator,
                title='Assignment status',
                notification='the assignment ({}) has been marked as {}'.format(instance.description,instance.get_status_display()),
                assignment=instance,
                )
            else:
                print('cant remember what was to go in here')
            

        else:
            print('this is an insert')
        
        

# @receiver(post_save,sender=Assignment)
# def new_assignments(sender,**kwargs):
#     print('you have added a new assignment did you notice am a post save method')


class Writer(models.Model):
    slug=models.SlugField(null=True)
    title=models.CharField(max_length=120)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='writers')
  

    def __str__(self):
        return self.user.username


    

