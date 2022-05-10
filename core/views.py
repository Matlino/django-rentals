from django.db.models import Window, F, RowRange
from django.db.models.functions import LastValue, FirstValue
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.conf import settings

from core.models import Rental, Reservation


def reservationsView(request):

    reservations = Reservation.objects.all(
    ).select_related(
        'rental'
    ).annotate(
        prev_reservation_id=Window(
            expression=FirstValue('pk'),
            partition_by=[F('rental')],
            order_by=F('checkin').asc(),
            frame=RowRange(start=-1, end=0)
        )
    ).order_by(
        'rental'
    )

    return TemplateResponse(request, 'core/reservation_list.html', {
        'reservations': reservations,
        'no_reservations': settings.CUSTOM_MSGS['no_reservations']
    })
