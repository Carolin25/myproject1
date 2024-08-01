from django.urls import path
from .views import hello_welcome

urlpatterns = [
    path('', hello_welcome, name='hello_welcome'),
]
