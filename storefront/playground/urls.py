from django.urls import path
from . import views


# URL COnf module
urlpatterns = [
    path("hello/", views.say_hello)
]