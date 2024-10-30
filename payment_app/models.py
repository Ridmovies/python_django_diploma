from django.db import models


class Payment(models.Model):
    # Todo add validators
    number = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    month = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    code = models.CharField(max_length=30)

