from time import sleep

from celery import shared_task

@shared_task
def simple_task(x, y):
    sleep(5)
    return x + y


@shared_task
def simple_beats_task(x, y):
    return x + y