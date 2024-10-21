from django.urls import path

from basket_app.views import (
    OrdersListView,
    BasketView,
    OrderDetailView,
    PaymentView,
)

urlpatterns = [
    path("basket", BasketView.as_view()),
    path("orders", OrdersListView.as_view()),
    path("order/<int:id>", OrderDetailView.as_view()),
    path("payment/<int:id>", PaymentView.as_view()),
]
