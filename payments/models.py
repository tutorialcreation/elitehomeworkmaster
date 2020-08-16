import stripe
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from assignments.models import Assignment
from django.dispatch import receiver
from django.db.models.signals import (
    post_save,post_migrate,post_init,
    post_delete,pre_delete,pre_init,
    pre_migrate,pre_save
)
import urllib
from authentication.models import Notification,User
from chat.models import ChatMessage,Thread
stripe.api_key=settings.STRIPE_SECRET_KEY


MEMBERSHIP_CHOICES=(
    ('Free','FREE'),
    ('Q1','Quote_One'),
    ('Q2','Quote Two'),
    ('Q3','Qutoe Three'),
)


    
# class Membership(models.Model):
#     slug=models.SlugField()
#     membership_type=models.CharField(max_length=54,choices=MEMBERSHIP_CHOICES,default='Free')
#     price=models.IntegerField(default=12)
#     payment_status=models.BooleanField(default=False)
#     stripe_plan_id=models.CharField(max_length=40)

#     def __str__(self):
#         return self.membership_type 


# class UserMembership(models.Model):
#     user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     stripe_customer_id=models.CharField(max_length=40)
#     membership=models.ForeignKey(Membership,on_delete=models.SET_NULL,null=True,default=4)

#     # def __str__(self):
#     #     return self.user
        

# def post_save_usermembership_create(sender,instance,created,*args,**kwargs):
#     if created:
#         UserMembership.objects.get_or_create(user=instance)   

#     user_membership, created = UserMembership.objects.get_or_create(user=instance)

#     if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id=='':
#         new_customer_id=stripe.Customer.create(email=instance.email)
#         user_membership.stripe_customer_id=new_customer_id['id']
#         user_membership.save()

# post_save.connect(post_save_usermembership_create,sender=settings.AUTH_USER_MODEL)




# class Subscription(models.Model):
#     user_membership=models.ForeignKey(UserMembership,on_delete=models.CASCADE)
#     stripe_subscription_id=models.CharField(max_length=40)
#     active=models.BooleanField(default=True)

#     def  __str__(self):
#         return self.user_membership.user.username


class Order(models.Model):
    token=models.CharField(max_length=250,blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='USD Order Total')
    emailAddress=models.EmailField(max_length=250,blank=True,verbose_name='Email Address')
    created=models.DateTimeField(auto_now_add=True)
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE,null=True,blank=True)
    paid=models.BooleanField(default=False)
    writer=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    support=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True, related_name='support_order')
    client=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='client_order')

    class Meta:
        db_table='Order'
        ordering=['-created']

    def __str__(self):
        return str(self.id)

@receiver(post_save,sender=Order)
def new_order(sender,instance,**kwargs):
    print('you have fired up a new order')
    if kwargs['created']:
            objects, threads=Thread.objects.get_or_new(instance.client,instance.support)
            ChatMessage.objects.create(
                thread=objects,
                user=instance.client,
                title='A new order',
                notification='Payment has been made by client {}'.format(instance.client),
                assignment=instance.assignment,
                payment=instance
            )
    
            
class OrderItem(models.Model):
    assignment=models.CharField(max_length=250)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)

    class Meta:
        db_table='OrderItem'

    
    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.assignment