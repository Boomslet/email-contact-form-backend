from rest_framework import serializers

from .models import Contact
from copy import copy


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
