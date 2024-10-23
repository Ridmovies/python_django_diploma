from django.urls import path, include

from catalog_app.views import (
    PopularProductsListApi,
    LimitedProductsListApi,
    BannerListApi,
    SaleApi,
    CategoriesListView,
    CatalogView,
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
