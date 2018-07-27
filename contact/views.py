from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactSerializer


RECIPIENTS = ['m.boon93@hotmail.com']


class ContactView(ModelViewSet):
    serializer_class = ContactSerializer

    def send_contact(self, request):

        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_address = request.POST.get('from_address', '')
        if subject and message and from_address:
            try:
                send_mail(subject, message, from_address,
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return Response({})
        return Response({})
