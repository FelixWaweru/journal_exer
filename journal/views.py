from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model

User = get_user_model()


    
# Views
def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'index.html', {})


class signup(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Message
def logged_in_message(sender, user, request, **kwargs):
    messages.success(request, "Welcome Back")


def logged_out_message(sender, user, request, **kwargs):
    messages.success(request, "Successfully Logged Out")


def log_in_failed(sender, request, **kwargs):
    messages.error(request, "Login Failed. Please check your details and try again")


user_logged_in.connect(logged_in_message)
user_logged_out.connect(logged_out_message)
user_login_failed.connect(log_in_failed)
