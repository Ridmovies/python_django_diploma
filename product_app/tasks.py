from time import sleep

from celery import shared_task

from product_app.services import update_product_avg_rating


@shared_task
def simple_task(x, y):
    sleep(5)
    return x + y


@shared_task
def simple_beats_task(x, y):
    return x + y


@shared_task
def task_update_product_avg_rating(product_id: int):
    update_product_avg_rating(product_id)


