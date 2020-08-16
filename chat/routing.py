#chat routing 
from django.urls import re_path

from .consumers import SupportToCustomerConsumer,SupportToWriterConsumer

websocket_urlpatterns=[
    # re_path(r'^ws/chat/(?P<username>[\w.@+-]+)/$',SupportToWriterConsumer),
    re_path(r'^ws/chat/writers/(?P<username>[\w.@+-]+)/$',SupportToWriterConsumer),
    
]