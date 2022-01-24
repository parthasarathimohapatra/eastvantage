from django.db import models

# Create your models here.

class Address(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    is_deleted = models.CharField(max_length=10, default="n")