from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Thing(models.Model):
    # name = models.CharField(
    #     max_length=30,
    #     unique=True,
    #     blank=False,
    #     error_messages={
    #         'unique': 'This name is already in use.'
    #     }
    # )

    # description = models.TextField(
    #     blank=True,
    #     max_length=120,
    # )

    # quantity = models.IntegerField(
    #     validators=[
    #         MinValueValidator(limit_value=0, message="Quantity must be at least 0."),
    #         MaxValueValidator(limit_value=100, message="Quantity must not exceed 100.")
    #     ]
    # )
    pass