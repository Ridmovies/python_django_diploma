from yookassa import Payment, Configuration
import uuid


Configuration.account_id = "482541"
Configuration.secret_key = "test_UR6XrxqsPiSVecyqR5R4EZHPQtRhBYd1UYvHXUu2HJs"
idempotence_key = str(uuid.uuid4())


def get_confirmation_url(value: str, description: str):
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
          "return_url": "http://127.0.0.1:8000/payment/success/"
        },
        "description": description,
        "refundable": False,
        "test": True
    }, idempotence_key)

    # get confirmation url
    confirmation_url = payment.confirmation.confirmation_url
    print(f"{confirmation_url=}")
    return confirmation_url
