from django.urls import path
from views import Chat_view

urlpatterns = [
    path('', Chat_view.as_view())
]