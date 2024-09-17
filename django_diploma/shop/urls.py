from django.urls import path

from shop.views import (
    ProductListView,
    CategoryListView
)


app_name = "shop"

urlpatterns = [
    # path("", hello, name="hello"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("category/", CategoryListView.as_view(), name="category_list"),
]
