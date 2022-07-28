from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, CustomUserCreationForm, EntrySumbission
from .models import Entry, Member, Share
from .tasks import email_send
from django.utils import timezone
from datetime import datetime
from django.urls import reverse_lazy
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

User = get_user_model()


    
# Views
def home(request):
    form = EntrySumbission()
    if request.method == 'POST' and request.user.is_anonymous == False:
        form = EntrySumbission(request.POST)
        if form.is_valid():
            user_id = request.user
            text_post = str(form.cleaned_data.get('submission'))

            entry = Entry.objects.create(user_id=user_id, text_post=text_post)
            member = Member.objects.get(pk=request.user.id)
            member.last_post = timezone.localtime()
            if len(text_post)>500:
                messages.error(request, "Journal Entry Too Long")
            else:
                entry.save()
                member.save()

                messages.success(request, "Journal Entry Submitted")
    elif request.method == 'POST' and request.user.is_anonymous:
        messages.error(request, "Kindly Login To Submit Entry")
    
    try:
        entry = Entry.objects.filter(
            user_id=request.user).order_by('-entry_date')
        main_context = {
            'entries': entry,
            'entries_count':len(entry),
            'form': form
        }
        return render(request, 'index.html', main_context)

    except:
        main_context = {
            'entries': None,
            'entries_count': None,
            'form': form
        }
        return render(request, 'index.html', main_context)

class signup(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def celery_test(request):
    email_send.delay()
    # today = timezone.now()
    # yesterday = timezone.now() - timezone.timedelta(1)
    # all_entries = Entry.objects.filter(entry_date__range=[yesterday, today]).order_by('?')

    # final_entries = all_entries.values_list(
    #     'text_post', flat=True)
    
    # new_share = Share.objects.create(
    #     entry_id=all_entries[0], shared_with=request.user)
    # new_share.save()

    # print(all_entries[0])
    return HttpResponse("Complete")

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
