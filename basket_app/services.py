from rest_framework.request import Request

from basket_app.models import Basket


def get_or_create_basket(request: Request):
    if request.user.is_authenticated:
        basket: Basket = Basket.objects.get(user=request.user)
        return basket

    elif request.user.is_anonymous:
        basket, _ = Basket.objects.get_or_create(session_key=request.session.session_key)
        return basket




