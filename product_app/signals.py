from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from product_app.models import Review, Product
from product_app.services import update_product_avg_rating


@receiver(post_save, sender=Review)
def update_reviews_count(sender, instance, created, **kwargs):
    if created:
        # Обновление среднего рейтинга через сигналы
        update_product_avg_rating(instance.product_id)
        # Если отзыв был создан, увеличиваем счетчик
        instance.product.reviews_count += 1
        # Сохраняем изменения в базе данных
        instance.product.save(update_fields=['reviews_count'])


@receiver(post_save, sender=Product)
def clear_cache(sender, instance, created, **kwargs):
    if created:
        # Сброс кэша для всех моделей
        cache.clear()
