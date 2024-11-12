from django.urls import path

from basket_app.views import (
    BasketView,
    OldOrdersListView,
    OrderDetailView,
    OrdersListView,
    celery_test,
)

app_name = "basket_app"

urlpatterns = [
    path("basket", BasketView.as_view(), name="basket"),
    path("orders", OrdersListView.as_view(), name="orders"),
    path("oldorders", OldOrdersListView.as_view(), name="oldorders"),
    path("order/<int:id>", OrderDetailView.as_view(), name="order_detail"),
    path("celery_test", celery_test),
]
