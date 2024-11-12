from django.urls import path, include

from product_app.views import (
    ProductDetailApiView,
    AddProductReviewApiView,
    TagsListView,
)


app_name = "product"

urlpatterns = [
    path("tags/", TagsListView.as_view(), name="tags"),
    path("product/<int:id>/", ProductDetailApiView.as_view(), name="product_detail"),
    path(
        "product/<int:id>/reviews", AddProductReviewApiView.as_view(), name="add_review"
    ),
]
