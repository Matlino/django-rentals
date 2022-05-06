from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.conf import settings

from core.models import Rental, Reservation


def rentalsView(request):
    return TemplateResponse(request, 'core/rental_list.html', {
        'rentals': Rental.objects.all(),
        'no_rentals': settings.CUSTOM_MSGS['no_rentals']
    })


