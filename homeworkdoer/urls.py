from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from .views import IndexView,AboutView,contacts,workflow,policy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('authentication/',include('authentication.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/',TemplateView.as_view(template_name='profile.html'), name='user_profile'),
    path('',IndexView,name='index'),
    path('about/',AboutView,name='about'),
    path('contact/',contacts,name='contacts'),
    path('workflow/',workflow,name='workflow'),
    path('policy/',policy,name='policy'),
    # path('chatbot/',chatbot,name='chatbot'),
    path('assignments/',include('assignments.urls')),
    path('payments/',include('payments.urls',namespace='payments')),
    path('paypal/',include('paypal.standard.ipn.urls')),
    path('writers/',include('writers.urls',namespace='writers')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
