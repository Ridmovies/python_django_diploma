from django.urls import path
from django.views.decorators.cache import cache_page

from catalog_app.views import (
    BannerListApi,
    CatalogView,
    CategoriesListView,
    LimitedProductsListApi,
    PopularProductsListApi,
    SaleApi,
)
from python_django_diploma.settings import CACHE_MIDDLEWARE_SECONDS

app_name = "catalog"

urlpatterns = [
    path("products/popular/",
         cache_page(CACHE_MIDDLEWARE_SECONDS)(PopularProductsListApi.as_view()),
         name="popular"),
    path("products/limited/",
         cache_page(CACHE_MIDDLEWARE_SECONDS)(LimitedProductsListApi.as_view()),
         name="limited"),
    path("banners/",
         cache_page(CACHE_MIDDLEWARE_SECONDS)(BannerListApi.as_view()),
         name="banners"),
    path("sales/",
         cache_page(CACHE_MIDDLEWARE_SECONDS)(SaleApi.as_view()),
         name="sales"),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("catalog/", CatalogView.as_view(), name="catalog_view"),
]
