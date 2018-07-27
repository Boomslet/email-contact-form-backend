from django.db import models
from rest_framework import serializers


class Contact(models.Model):
  
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=100000)
    from_address = models.CharField(max_length=150)

    def __str__(self):
        return self.from_address
