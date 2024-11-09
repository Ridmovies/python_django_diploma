from celery import shared_task

from basket_app.models import Order


@shared_task
def simple_add(x, y):
    return x + y
