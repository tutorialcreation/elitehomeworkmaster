from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from chat.models import Thread,ChatMessage
from authentication.models import User
from authentication.models import Notification
from chat.chatbot import chatbot_query

# Create your views here.
def IndexView(request):
    context={}
    if request.method == 'POST':
        content = request.POST.get('content')
        context['reply']=chatbot_query(content)
        return render(request,'index.html',context)
    
    if request.user.is_staff or request.user.is_superuser:
        return redirect(reverse('chat:orders'))
    else:
        return render(request,'index.html',context)

def AboutView(request):
    return render(request,'about.html')


def contacts(request):
    return render(request,'contact.html')

def workflow(request):
    return render(request,'workflow.html')


def policy(request):
    return render(request,'policy.html')
    
