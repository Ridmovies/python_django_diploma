from django.http import HttpRequest, HttpResponse


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello")



# class ProductDetailApiView(