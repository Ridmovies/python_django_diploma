from django.urls import path, include
from rest_framework import routers

from shop.views import (
    # ProductListView,
    CategoryListView,
    UserViewSet,
    GroupViewSet,
    ProductViewSet,
    CategoryViewSet,
)

app_name = "shop"

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("products/", ProductListView.as_view(), name="product_list"),
    path("category/", CategoryListView.as_view(), name="category_list"),
]
