import os

from celery import Celery
from celery.schedules import crontab
# from product_app import tasks

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_django_diploma.settings")

app = Celery("python_django_diploma")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-monday-morning': {
        'task': 'product_app.tasks.simple_beats_task',
        'schedule': crontab(minute='*/1'),
        'args': (16, 16),
    },
}
