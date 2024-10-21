from rest_framework import serializers


class CreditCardValidator(object):
    def __init__(self, min_length=16, max_length=19, ends_with_odd_digit=True):
        self.min_length = min_length
        self.max_length = max_length
        self.ends_with_odd_digit = ends_with_odd_digit

    def validate(self, value):
        if len(value) < self.min_length or len(value) > self.max_length:
            raise serializers.ValidationError(
                "Credit card number must be between {} and {} digits long.".format(self.min_length, self.max_length))

        if not self.ends_with_odd_digit:
            return True

        last_digit = int(value[-1])
        if last_digit % 2 == 1:
            return True
        else:
            raise serializers.ValidationError("Credit card number must end with an odd digit.")