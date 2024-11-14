from django.apps import AppConfig
from django.db.models.signals import post_save
from django.utils.module_loading import import_module


class ProductAppConfig(AppConfig):
    name = 'product_app'

    # def ready(self):
    #     from .signals import update_reviews_count
