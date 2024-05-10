# routing.py in your app directory

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/driver_notifications/', consumers.RideNotificationConsumer.as_asgi()),
]
