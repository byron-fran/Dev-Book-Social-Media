from . import consumers
from django.urls import path

websocket_urlpatterns = [
    path('ws/comments/<int:post_id>/', consumers.CommentConsumer.as_asgi()),
]