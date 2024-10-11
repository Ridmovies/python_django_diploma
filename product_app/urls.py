from django.urls import path, include

from product_app.views import ProductDetailApiView, AddProductReviewApiView

urlpatterns = [
    path("product/<int:id>/", ProductDetailApiView.as_view()),
    path("product/<int:id>/reviews", AddProductReviewApiView.as_view()),
]
