from django.db import models


class Rate(models.Model):
    currency_type = models.CharField(max_length=5)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    source = models.CharField(max_length=64)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class ContactUS(models.Model):
    email_from = models.EmailField(max_length=320)
    subject = models.CharField(max_length=64)
    message = models.TextField()


class Source(models.Model):
    source_name = models.CharField(max_length=64)
    source_url = models.URLField(max_length=256)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
