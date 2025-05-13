from django.urls import path
from .views import Chat_view

urlpatterns = [
    path('api/chats/', Chat_view.as_view(), name='chat_view'),
]