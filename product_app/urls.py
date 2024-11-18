from django.urls import include, path

from product_app.views import (
    AddProductReviewApiView,
    ProductDetailApiView,
    TagsListView,
    CeleryTestApi,
)

app_name = "product"

urlpatterns = [
    path("tags/", TagsListView.as_view(), name="tags"),
    path("product/<int:id>/", ProductDetailApiView.as_view(), name="product_detail"),
    path(
        "product/<int:id>/reviews", AddProductReviewApiView.as_view(), name="add_review"
    ),
    path("celery/", CeleryTestApi.as_view())
]
