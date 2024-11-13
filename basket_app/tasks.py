from celery import shared_task


@shared_task
def simple_add(x, y):
    return x + y


@shared_task
def my_scheduled_task():
    print("Задача выполнена!")
