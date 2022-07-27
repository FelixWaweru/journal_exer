from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task(bind=True)
def email_send(self):
    for i in range(5):
        print(i)
    return ("DONE :)")
