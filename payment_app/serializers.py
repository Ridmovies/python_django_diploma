from rest_framework import serializers

from basket_app.validators import CreditCardValidator
from payment_app.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    number = serializers.CharField(
        validators=[CreditCardValidator(ends_with_odd_digit=True)],
    )

    class Meta:
        model = Payment
        fields = (
            "number",
            "name",
            "month",
            "year",
            "code",
        )
