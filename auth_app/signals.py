from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from auth_app.models import Profile
from basket_app.models import Basket


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Basket.objects.create(user=instance)


# @receiver(post_save, sender=Review)
# def update_reviews_count(sender, instance, created, **kwargs):
#     if created:
#         # Обновление среднего рейтинга через сигналы
#         update_product_avg_rating(instance.product_id)
#         # Если отзыв был создан, увеличиваем счетчик
#         instance.product.reviews_count += 1
#         # Сохраняем изменения в базе данных
#         instance.product.save(update_fields=['reviews_count'])