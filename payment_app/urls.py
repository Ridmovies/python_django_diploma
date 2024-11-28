from django.urls import path

from payment_app.views import PaymentNotification

urlpatterns = [
    path("payments/<str:payment_id>/success", PaymentNotification.as_view()),
]
