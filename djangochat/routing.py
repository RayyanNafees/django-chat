from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from django.core.asgi import get_asgi_application
from chat import consumers

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/', consumers.ChatApplication.as_asgi())
        ])
    )
})