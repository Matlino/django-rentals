from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from core.models import Reservation, Rental


class RentalTest(TestCase):

    def test_no_rentals(self):
        url = reverse('rentals')
        resp = self.client.get(url)

        self.assertContains(resp, settings.CUSTOM_MSGS['no_rentals'])

    def test_reservation_data_display(self):
        rental_name = 'Test rental'
        rental = Rental.objects.create(name=rental_name)
        r1 = Reservation.objects.create(checkin='2022-01-01', checkout='2022-01-03', rental=rental)
        r2 = Reservation.objects.create(checkin='2022-01-06', checkout='2022-01-07', rental=rental)
        r3 = Reservation.objects.create(checkin='2022-01-04', checkout='2022-01-05', rental=rental)
        url = reverse('rentals')
        resp = self.client.get(url)

        self.assertInHTML(f"""
            <tr>
                <td>{rental_name}</td>
                <td>{r1.id}</td>
                <td>2022-01-01</td>
                <td>2022-01-03</td>
                <td>-</td>
            </tr>
            <tr>
                <td>{rental_name}</td>
                <td>{r3.id}</td>
                <td>2022-01-04</td>
                <td>2022-01-05</td>
                <td>{r1.id}</td>
            </tr>
            <tr>
                <td>{rental_name}</td>
                <td>{r2.id}</td>
                <td>2022-01-06</td>
                <td>2022-01-07</td>
                <td>{r3.id}</td>
            </tr>
        """, resp.content.decode(resp.charset))
