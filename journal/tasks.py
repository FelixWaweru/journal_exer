from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from .models import Member, Entry, Share
from django.utils import timezone

@shared_task(bind=True)
def email_send(self):
    today = timezone.now()
    yesterday = timezone.now() - timezone.timedelta(1)

    # Get all users with entries from past 24hrs
    all_recepients = Member.objects.filter(last_post__range=[yesterday, today])

    # Get all entries from past 24hrs as list and shuffle them
    all_entries = Entry.objects.filter(entry_date__range=[yesterday, today]).order_by('?')

    entries_list = all_entries.values_list(
        'text_post', flat=True)

    i = 0
    for user in all_recepients:
        # Email Sender
        subject = "Your Daily Journal"
        body = entries_list[i]
        sender = "hello.from@felix.waweru"
        recepient = [user.email]

        send_mail(subject, body, sender, recepient, fail_silently=False)

        new_share = Share.objects.create(
            entry_id=all_entries[i], shared_with=user)
        new_share.save()

        print("Email Sent to: " + str(user.email))

        i += 1

    return ('All Emails Sent')
