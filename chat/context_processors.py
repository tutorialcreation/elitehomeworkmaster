from chat.forms import ComposeForm
from django.shortcuts import render
from chat.models import Thread,ChatMessage

def chat_form(request):
    compose_form=ComposeForm()
    context_dict={
        'chat_form':compose_form
    }
    
    return context_dict


def messages(request):
    # if request.user.is_authenticated:
    # other_username='alfayo'
    message_retreive=Thread.objects.all()

    # import pdb; pdb.set_trace()
    if message_retreive is not None:
        messagesets=message_retreive
        return dict(messagesets=messagesets)


# def notifications()