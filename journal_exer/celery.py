from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'journal_exer.settings')

app = Celery('journal_exer')
app.conf.enable_utc = False
app.conf.update(timezone = 'Africa/Nairobi')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    '12pm-daily-email-send':{
        'task': 'journal.tasks.email_send',
        'schedule': crontab(minute='*/2'), # crontab(hour=12, minute=00) Run daily at 12 pm
        # 'args': ''
    }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
