from django.urls import path

from basket_app.views import OrdersListView, BasketView

urlpatterns = [
    path("basket", BasketView.as_view()),
    path("orders/", OrdersListView.as_view()),
]
