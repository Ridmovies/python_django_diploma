from django.http import HttpRequest, HttpResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductDetailApiView(APIView):
    def get(self, request: Request, id: int) -> Response:
        return Response({"hi": "hi"})
