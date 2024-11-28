import os
import uuid

from django.conf import settings
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.response import Response
from yookassa import Configuration, Payment

load_dotenv()
Configuration.account_id = os.getenv("ACCOUNT_ID")
Configuration.secret_key = os.getenv("SECRET_KEY")

idempotence_key = str(uuid.uuid4())


def get_confirmation_url(value: str, description: str, order_id: int):
    """ Генерация ссылки на оплату """
    return_url = settings.BASE_URL
    payment = Payment.create(
        {
            "amount": {"value": value, "currency": "RUB"},
            "payment_method_data": {"type": "bank_card"},
            "confirmation": {"type": "redirect", "return_url": return_url},
            "description": description,
            "refundable": False,
            "capture": True,
            "metadata": {"orderId": order_id},
            "test": True,
        },
        idempotence_key,
    )

    # get confirmation url
    try:
        confirmation_url = payment.confirmation.confirmation_url
    except AttributeError:
        return Response(
            {"message": "You can't pay this order again"},
            status=status.HTTP_409_CONFLICT,
        )
    return confirmation_url


def get_payment_info(payment_id: str):
    """ Получение информации о платеже """
    payment = Payment.find_one(payment_id)
    return payment


