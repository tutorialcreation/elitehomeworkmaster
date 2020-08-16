from .models import Assignment
from authentication.models import Notification
from chat.models import ChatMessage,Thread

def get_notifications(request):
    notificationset=Thread.objects.all()
    welcome=Notification.objects.all()
    return dict(notificationset=notificationset,welcome=welcome)


def get_first_assignment(request):
    assignment=Assignment.objects.all().first()
    return dict(assignment=assignment)

