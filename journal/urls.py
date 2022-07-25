from django.urls import path
from . import  views

# URL config
urlpatterns = [
    path('',  views.home, name = 'home'),
    path('signup/', views.signup.as_view(), name='signup'),
]
