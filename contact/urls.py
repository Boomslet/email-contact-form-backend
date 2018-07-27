from django.urls import path

from .views import ContactView

urlpatterns = [
    path('contact/', ContactView.as_view({
        'post': 'send_contact',
    }), name='submit_contact'),
]
