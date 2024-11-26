from django.urls import path

from payment_app.views import (
    # PaymentConfirmView,
    PaymentInfoView,
    PaymentListView,
    PaymentNotification,
)

urlpatterns = [
    path("payments", PaymentListView.as_view()),
    path("payments/<str:payment_id>/success", PaymentNotification.as_view()),
    path("payments/<str:payment_id>", PaymentInfoView.as_view()),
    # path("payments/<str:payment_id>/capture", PaymentConfirmView.as_view()),
    # path("payment/<int:id>", PaymentView.as_view()),
]
