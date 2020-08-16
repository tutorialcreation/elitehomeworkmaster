from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter,URLRouter
import chat.routing
from chat.consumers import SupportToWriterConsumer

application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter( 
            [
                url(r'^chat/channel/(?P<username>[\w.@+-]+)/(?P<pk>[0-9]+)/',SupportToWriterConsumer),
            ]
            # chat.routing.websocket_urlpatterns
        )
    )
})