from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Coba(models.Model):
    nama = models.CharField(max_length=255)
    usia = models.DecimalField(max_digits=10, decimal_places=2)

