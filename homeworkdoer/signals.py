from django.db.models.signals import (
    post_delete,post_init,post_migrate,post_save,
    pre_delete,pre_init,pre_migrate,pre_save
)
from django.core.signals import (
    request_finished,request_started,got_request_exception
)

from assignments.models import (
    Assignment
)

from chat.models import(
    ChatMessage,Thread
)

from payments.models import(
    Membership,UserMembership,Subscription
)

from writers.models import (
    WritersJoin,Document
)


from django.dispatch import receiver,Signal




######################
# Assignment signals #
######################
counter= Signal(providing_args=[])


######################
# assignment signals #
######################



@receiver(post_save,sender=Assignment)
def assignment_post_save_signal(sender,instance,**kwargs):
    print('this is the assignment post save signal')


@receiver(post_init,sender=Assignment)
def assignment_post_init_signal(sender,instance,**kwargs):
    print('this is the assignment post init signal')

@receiver(post_delete,sender=Assignment)
def assignment_post_delete_signal(sender,instance,**kwargs):
    print('this is the assignment post delete signal')

@receiver(post_migrate,sender=Assignment)
def assignment_post_migrate_signal(sender,instance,**kwargs):
    print('this is the assignment post migrate signal')

@receiver(pre_save,sender=Assignment)
def assignment_pre_save_signal(sender,instance,**kwargs):
    print('this is the assignment pre save signal')

@receiver(pre_init,sender=Assignment)
def assignment_pre_init_signal(sender,instance,**kwargs):
    print('this is the assignment pre init signal')

@receiver(pre_delete,sender=Assignment)
def assignment_pre_delete_signal(sender,instance,**kwargs):
    print('this is the assignment pre delete signal')

@receiver(pre_migrate,sender=Assignment)
def assignment_pre_migrate_signal(sender,instance,**kwargs):
    print('this is the assignment pre migrate signal')

@receiver(request_finished)
def assignment_request_finished_signal(sender,**kwargs):
    print('this is the assignment request finished signal')

@receiver(request_started)
def assignment_request_started_signal(sender,**kwargs):
    print('this is the assignment request started signal')

@receiver(got_request_exception)
def assignment_got_request_exception_signal(sender,**kwargs):
    print('this is the assignment got request exception signal')


###################
# ChatMessage signals #
###################
counter=Signal(providing_args=[])




################
# ChatMessage signals #
################
@receiver(post_save,sender=ChatMessage)
def chatmessage_post_save_signal(sender,instance,**kwargs):
    print('this is the chatmessage post save signal')


@receiver(post_init,sender=ChatMessage)
def chatmessage_post_init_signal(sender,instance,**kwargs):
    print('this is the chatmessage post init signal')

@receiver(post_delete,sender=ChatMessage)
def chatmessage_post_delete_signal(sender,instance,**kwargs):
    print('this is the chatmessage post delete signal')

@receiver(post_migrate,sender=ChatMessage)
def chatmessage_post_migrate_signal(sender,instance,**kwargs):
    print('this is the chatmessage post migrate signal')

@receiver(pre_save,sender=ChatMessage)
def chatmessage_pre_save_signal(sender,instance,**kwargs):
    print('this is the chatmessage pre save signal')

@receiver(pre_init,sender=ChatMessage)
def chatmessage_pre_init_signal(sender,instance,**kwargs):
    print('this is the chatmessage pre init signal')

@receiver(pre_delete,sender=ChatMessage)
def chatmessage_pre_delete_signal(sender,instance,**kwargs):
    print('this is the chatmessage pre delete signal')

@receiver(pre_migrate,sender=ChatMessage)
def chatmessage_pre_migrate_signal(sender,instance,**kwargs):
    print('this is the chatmessage pre migrate signal')

@receiver(request_finished)
def chatmessage_request_finished_signal(sender,**kwargs):
    print('this is the chatmessage finished signal')

@receiver(request_started)
def chatmessage_request_started_signal(sender,**kwargs):
    print('this is the chatmessage request started signal')

@receiver(got_request_exception)
def chatmessage_got_request_exception_signal(sender,**kwargs):
    print('this is the chatmessage got request exception signal')



################
# thread signals #
################
counter=Signal(providing_args=[])

################
# thread signals #
################
@receiver(post_save,sender=Thread)
def thread_post_save_signal(sender,instance,**kwargs):
    print('this is the thread post save signal')


@receiver(post_init,sender=Thread)
def thread_post_init_signal(sender,instance,**kwargs):
    print('this is the thread post init signal')

@receiver(post_delete,sender=Thread)
def thread_post_delete_signal(sender,instance,**kwargs):
    print('this is the thread post delete signal')

@receiver(post_migrate,sender=Thread)
def thread_post_migrate_signal(sender,instance,**kwargs):
    print('this is the thread post migrate signal')

@receiver(pre_save,sender=Thread)
def thread_pre_save_signal(sender,instance,**kwargs):
    print('this is the thread pre save signal')

@receiver(pre_init,sender=Thread)
def thread_pre_init_signal(sender,instance,**kwargs):
    print('this is the thread pre init signal')

@receiver(pre_delete,sender=Thread)
def thread_pre_delete_signal(sender,instance,**kwargs):
    print('this is the thread pre delete signal')

@receiver(pre_migrate,sender=Thread)
def thread_pre_migrate_signal(sender,instance,**kwargs):
    print('this is the thread pre migrate signal')

@receiver(request_finished)
def thread_request_finished_signal(sender,**kwargs):
    print('this is the thread request finished signal')

@receiver(request_started)
def thread_request_started_signal(sender,**kwargs):
    print('this is the thread request started signal')

@receiver(got_request_exception)
def thread_got_request_exception_signal(sender,**kwargs):
    print('this is the thread got request exception signal')


######################
# Membership signals #
######################
counter= Signal(providing_args=[])


######################
# Membership signals #
######################



@receiver(post_save,sender=Membership)
def membership_post_save_signal(sender,instance,**kwargs):
    print('this is the membership post save signal')


@receiver(post_init,sender=Membership)
def membership_post_init_signal(sender,instance,**kwargs):
    print('this is the membership post init signal')

@receiver(post_delete,sender=Membership)
def membership_post_delete_signal(sender,instance,**kwargs):
    print('this is the membership post delete signal')

@receiver(post_migrate,sender=Membership)
def membership_post_migrate_signal(sender,instance,**kwargs):
    print('this is the membership post migrate signal')

@receiver(pre_save,sender=Membership)
def membership_pre_save_signal(sender,instance,**kwargs):
    print('this is the membership pre save signal')

@receiver(pre_init,sender=Membership)
def membership_pre_init_signal(sender,instance,**kwargs):
    print('this is the membership pre init signal')

@receiver(pre_delete,sender=Membership)
def membership_pre_delete_signal(sender,instance,**kwargs):
    print('this is the membership pre delete signal')

@receiver(pre_migrate,sender=Membership)
def membership_pre_migrate_signal(sender,instance,**kwargs):
    print('this is the membership pre migrate signal')

@receiver(request_finished)
def membership_request_finished_signal(sender,**kwargs):
    print('this is the membership request finished signal')

@receiver(request_started)
def membership_request_started_signal(sender,**kwargs):
    print('this is the membership request started signal')

@receiver(got_request_exception)
def membership_got_request_exception_signal(sender,**kwargs):
    print('this is the membership got request exception signal')


###################
# UserMembership signals #
###################
counter=Signal(providing_args=[])




################
# ChatMessage signals #
################
@receiver(post_save,sender=UserMembership)
def usermembership_post_save_signal(sender,instance,**kwargs):
    print('this is the usermembership post save signal')


@receiver(post_init,sender=UserMembership)
def usermembership_post_init_signal(sender,instance,**kwargs):
    print('this is the usermembership post init signal')

@receiver(post_delete,sender=UserMembership)
def usermembership_post_delete_signal(sender,instance,**kwargs):
    print('this is the usermembership post delete signal')

@receiver(post_migrate,sender=UserMembership)
def usermembership_post_migrate_signal(sender,instance,**kwargs):
    print('this is the usermembership post migrate signal')

@receiver(pre_save,sender=UserMembership)
def usermembership_pre_save_signal(sender,instance,**kwargs):
    print('this is the usermembership pre save signal')

@receiver(pre_init,sender=UserMembership)
def usermembership_pre_init_signal(sender,instance,**kwargs):
    print('this is the usermembership pre init signal')

@receiver(pre_delete,sender=UserMembership)
def usermembership_pre_delete_signal(sender,instance,**kwargs):
    print('this is the usermembership pre delete signal')

@receiver(pre_migrate,sender=UserMembership)
def usermembership_pre_migrate_signal(sender,instance,**kwargs):
    print('this is the usermembership pre migrate signal')

@receiver(request_finished)
def usermembership_request_finished_signal(sender,**kwargs):
    print('this is the usermembership finished signal')

@receiver(request_started)
def usermembership_request_started_signal(sender,**kwargs):
    print('this is the usermembership request started signal')

@receiver(got_request_exception)
def usermembership_got_request_exception_signal(sender,**kwargs):
    print('this is the usermembership got request exception signal')



################
# Subscription signals #
################
counter=Signal(providing_args=[])

################
# Subscription signals #
################
@receiver(post_save,sender=Subscription)
def subscription_post_save_signal(sender,instance,**kwargs):
    print('this is the subscription post save signal')


@receiver(post_init,sender=Subscription)
def subscription_post_init_signal(sender,instance,**kwargs):
    print('this is the subscription post init signal')

@receiver(post_delete,sender=Subscription)
def subscription_post_delete_signal(sender,instance,**kwargs):
    print('this is the subscription post delete signal')

@receiver(post_migrate,sender=Subscription)
def subscription_post_migrate_signal(sender,instance,**kwargs):
    print('this is the subscription post migrate signal')

@receiver(pre_save,sender=Subscription)
def subscription_pre_save_signal(sender,instance,**kwargs):
    print('this is the  subscription pre save signal')

@receiver(pre_init,sender=Subscription)
def subscription_pre_init_signal(sender,instance,**kwargs):
    print('this is the subscription pre init signal')

@receiver(pre_delete,sender=Subscription)
def subscription_pre_delete_signal(sender,instance,**kwargs):
    print('this is the subscription pre delete signal')

@receiver(pre_migrate,sender=Subscription)
def subscription_pre_migrate_signal(sender,instance,**kwargs):
    print('this is the subscription pre migrate signal')

@receiver(request_finished)
def subscription_request_finished_signal(sender,**kwargs):
    print('this is the subscription request finished signal')

@receiver(request_started)
def subscription_request_started_signal(sender,**kwargs):
    print('this is the subscription request started signal')

@receiver(got_request_exception)
def subscription_got_request_exception_signal(sender,**kwargs):
    print('this is the subscription got request exception signal')


################
# WritersJoin signals #
################
counter=Signal(providing_args=[])

################
# WritersJoin signals #
################
@receiver(post_save,sender=WritersJoin)
def WritersJoin_post_save_signal(sender,instance,**kwargs):
    print('this is the WritersJoin post save signal')


@receiver(post_init,sender=WritersJoin)
def WritersJoin_post_init_signal(sender,instance,**kwargs):
    print('this is the WritersJoin post init signal')

@receiver(post_delete,sender=WritersJoin)
def WritersJoin_post_delete_signal(sender,instance,**kwargs):
    print('this is the WritersJoin post delete signal')

@receiver(post_migrate,sender=WritersJoin)
def WritersJoin_post_migrate_signal(sender,instance,**kwargs):
    print('this is the WritersJoin post migrate signal')

@receiver(pre_save,sender=WritersJoin)
def WritersJoin_pre_save_signal(sender,instance,**kwargs):
    print('this is the  WritersJoin pre save signal')

@receiver(pre_init,sender=WritersJoin)
def WritersJoin_pre_init_signal(sender,instance,**kwargs):
    print('this is the WritersJoin pre init signal')

@receiver(pre_delete,sender=WritersJoin)
def WritersJoin_pre_delete_signal(sender,instance,**kwargs):
    print('this is the WritersJoin pre delete signal')

@receiver(pre_migrate,sender=WritersJoin)
def WritersJoin_pre_migrate_signal(sender,instance,**kwargs):
    print('this is the WritersJoin pre migrate signal')

@receiver(request_finished)
def WritersJoin_request_finished_signal(sender,**kwargs):
    print('this is the WritersJoin request finished signal')

@receiver(request_started)
def WritersJoin_request_started_signal(sender,**kwargs):
    print('this is the WritersJoin request started signal')

@receiver(got_request_exception)
def WritersJoin_got_request_exception_signal(sender,**kwargs):
    print('this is the WritersJoin got request exception signal')



################
# Document signals #
################
counter=Signal(providing_args=[])

################
# Document signals #
################
@receiver(post_save,sender=Document)
def Document_post_save_signal(sender,instance,**kwargs):
    print('this is the Document post save signal')


@receiver(post_init,sender=Document)
def Document_post_init_signal(sender,instance,**kwargs):
    print('this is the Document post init signal')

@receiver(post_delete,sender=Document)
def Document_post_delete_signal(sender,instance,**kwargs):
    print('this is the Document post delete signal')

@receiver(post_migrate,sender=Document)
def Document_post_migrate_signal(sender,instance,**kwargs):
    print('this is the Document post migrate signal')

@receiver(pre_save,sender=Document)
def Document_pre_save_signal(sender,instance,**kwargs):
    print('this is the  Document pre save signal')

@receiver(pre_init,sender=Document)
def Document_pre_init_signal(sender,instance,**kwargs):
    print('this is the Document pre init signal')

@receiver(pre_delete,sender=Document)
def Document_pre_delete_signal(sender,instance,**kwargs):
    print('this is the Document pre delete signal')

@receiver(pre_migrate,sender=Document)
def Document_pre_migrate_signal(sender,instance,**kwargs):
    print('this is the Document pre migrate signal')

@receiver(request_finished)
def Document_request_finished_signal(sender,**kwargs):
    print('this is the Document request finished signal')

@receiver(request_started)
def Document_request_started_signal(sender,**kwargs):
    print('this is the Document request started signal')

@receiver(got_request_exception)
def Document_got_request_exception_signal(sender,**kwargs):
    print('this is the Document got request exception signal')
