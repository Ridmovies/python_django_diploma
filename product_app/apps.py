from django.apps import AppConfig
from django.db.models.signals import post_save
from django.utils.module_loading import import_module


class ProductAppConfig(AppConfig):
    name = 'product_app'

    def ready(self):
        # Импортируем модели и функции только внутри метода ready()
        from .signals import update_reviews_count
        review = import_module('product_app.models').Review

        # Подключаем сигнал
        post_save.connect(update_reviews_count, sender=review)
