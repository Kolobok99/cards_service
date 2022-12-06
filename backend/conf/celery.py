import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

app = Celery('cards_service')

app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
	'check-expiration-date': {
		'task': "apps.polls.tasks.task_check_expiration_date",
		'schedule': crontab(hour=00, minute=1),
	},
}