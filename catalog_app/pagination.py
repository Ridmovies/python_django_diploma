import math

from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    # default page size
    page_size = settings.PAGE_SIZE
    # page size from query_param
    page_size_query_param = "limit"
    # max page size for query_param
    max_page_size = 10

    def get_page_number(self, request, page):
        # Получаем номер страницы из параметра currentPage
        current_page = request.query_params.get("currentPage", 1)
        return int(current_page)

    def get_paginated_response(self, data):
        return Response(
            {
                "currentPage": self.page.number,
                "lastPage": self.page.paginator.num_pages,
                "items": data,
            }
        )

    @staticmethod
    def _calculate_last_page(count, page_size):
        return math.ceil(count / page_size)
