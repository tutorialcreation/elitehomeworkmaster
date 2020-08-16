from chat.models import ChatMessage
from django.shortcuts import redirect

def chat(request):
    massages=ChatMessage.objects.all()[:3]
    return dict(massages=massages)
