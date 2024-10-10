from django.urls import path, include

from product_app.views import hello

urlpatterns = [
    path("product/<id:int>", hello),
]
