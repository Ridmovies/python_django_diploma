from django.http import HttpRequest, HttpResponse
from rest_framework.generics import RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from product_app.models import Product
from product_app.serializers import ProductFullSerializer


class ProductDetailApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
    lookup_field = 'id'
    # def get(self, request: Request, id: int) -> Response:
    #     product: Product = Product.objects.get(id=id)
    #     serialized = ProductFullSerializer(product, many=False)
    #     return Response(serialized.data)
