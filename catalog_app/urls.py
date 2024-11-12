from django.urls import include, path
from django.views.decorators.cache import cache_page

from catalog_app.views import (
    BannerListApi,
    CatalogView,
    CategoriesListView,
    LimitedProductsListApi,
    PopularProductsListApi,
    SaleApi,
)

app_name = "catalog"

urlpatterns = [
    path("products/popular/", PopularProductsListApi.as_view(), name="popular"),
    path("products/limited/", LimitedProductsListApi.as_view(), name="limited"),
    path("banners/", BannerListApi.as_view(), name="banners"),
    path("sales/", SaleApi.as_view(), name="sales"),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("catalog/", CatalogView.as_view(), name="catalog_view"),
]
