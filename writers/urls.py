from django.urls import path
from . import views

app_name='writers'

urlpatterns=[
    path('',views.index,name='index'),
    path('join/',views.writersjoin,name='join'),
    path('upload_data/',views.document_form,name='upload_my_files'),
    
]