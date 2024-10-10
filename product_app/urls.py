from django.urls import path, include

from product_app.views import ProductDetailApiView

urlpatterns = [
    path("product/<int:id>/", ProductDetailApiView.as_view()),
]
