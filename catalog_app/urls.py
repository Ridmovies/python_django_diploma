from django.urls import path, include

from catalog_app.views import (
    PopularProductsListApi,
    LimitedProductsListApi,
    BannerListApi,
    SaleApi,
    CategoriesListView,
)

urlpatterns = [
    path("products/popular/", PopularProductsListApi.as_view()),
    path("products/limited/", LimitedProductsListApi.as_view()),
    path("banners/", BannerListApi.as_view()),
    path("sales/", SaleApi.as_view()),
    path("categories/", CategoriesListView.as_view()),
]
