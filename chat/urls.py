from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf.urls import url

from .views import ThreadView, InboxView,room,index,IndexView,ClientView,WriterView,orders,reviews,search_assignment
# from assignments.views import search_assignment

app_name = 'chat'

urlpatterns = [
    path("", InboxView.as_view()),
    path("index/",index,name='index'),
    path("reviews/",reviews,name='review'),
    path('writers/',WriterView.as_view(),name='writer'),
    path('support/',ClientView.as_view(),name='client'),
    path('writers/dashboard/orders/',orders,name='orders'),
    # url(r'^index/', IndexView.as_view(template_name="search.html"),
    #                name='chat_room'),
    re_path(r"^channel/(?P<username>[\w.@+-]+)/(?P<pk>[0-9]+)/", ThreadView.as_view(),name='threads'),
    re_path(r"^channel/(?P<username>[\w.@+-]+)/(?P<pk>[0-9]+)/", search_assignment,name='search'),
    re_path(r'^(?P<room_name>[^/]+)/',room,name='room'),
]
