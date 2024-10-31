import os
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.response import Response

from yookassa import Payment, Configuration
import uuid

# Configuration.account_id = "482541"
# Configuration.secret_key = "test_UR6XrxqsPiSVecyqR5R4EZHPQtRhBYd1UYvHXUu2HJs"

load_dotenv()
Configuration.account_id = os.getenv('ACCOUNT_ID')
Configuration.secret_key = os.getenv('SECRET_KEY')

idempotence_key = str(uuid.uuid4())


def get_confirmation_url(value: str, description: str, order_id: int):
    return_url = "http://127.0.0.1:8000"
    payment = Payment.create({
        "amount": {
          "value": value,
          "currency": "RUB"
        },
        "payment_method_data": {
          "type": "bank_card"
        },
        "confirmation": {
          "type": "redirect",
          "return_url": return_url
        },
        "description": description,
        "refundable": False,
        "capture": True,
        "metadata": {
            "orderId": order_id
        },
        "test": True
    }, idempotence_key)

    # get confirmation url
    try:
        confirmation_url = payment.confirmation.confirmation_url
    except AttributeError:
        return Response({"message": "You can't pay this order again"}, status=status.HTTP_409_CONFLICT)
    return confirmation_url


def get_payment_info(payment_id: str):
    payment = Payment.find_one(payment_id)
    return payment


def get_payments_list():
    res = Payment.list()
    return res


def get_payment_confirm(payment_id: str):
    response = Payment.capture(
        # TODO HARDCODE
        payment_id,
        {
            "amount": {
                "value": "2.00",
                "currency": "RUB"
            }
        },
        idempotence_key
    )

