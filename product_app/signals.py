from django.db.models.signals import post_save
from django.dispatch import receiver

from product_app.models import Review


@receiver(post_save, sender=Review)
def update_reviews_count(sender, instance, created, **kwargs):
    if created:
        # Если отзыв был создан, увеличиваем счетчик
        instance.product.reviews_count += 1
        # Сохраняем изменения в базе данных
        instance.product.save(update_fields=['reviews_count'])
