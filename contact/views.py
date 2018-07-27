from django.core.mail import send_mail, BadHeaderError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactSerializer


RECIPIENTS = []


class ContactView(ModelViewSet):
    serializer_class = ContactSerializer

    def send_contact(self, request):
        subject = request.data['subject']
        message = request.data['message']
        from_address = request.data['from_address']
        
        if subject and message and from_address:
            try:
                send_mail(subject, message, from_address, RECIPIENTS)
            except BadHeaderError:
                return Response('Invalid header found.')
            return Response({})
        
        return Response({})
