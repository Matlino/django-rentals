from django.test import TestCase

from core.models import Rental, Reservation


class RentalTest(TestCase):

    def test_rental_creation(self):
        rental = Rental.objects.create(name='Test rental')
        self.assertTrue(isinstance(rental, Rental))
        self.assertEqual(rental.name, str(rental))


class ReservationTest(TestCase):

    def test_reservatin_ordering(self):
        rental = Rental.objects.create(name='Test rental')
        r1 = Reservation.objects.create(checkin='2022-01-01', checkout='2022-01-03', rental=rental)
        r2 = Reservation.objects.create(checkin='2022-01-06', checkout='2022-01-07', rental=rental)
        r3 = Reservation.objects.create(checkin='2022-01-04', checkout='2022-01-05', rental=rental)

        reservations = rental.reservation_set.all()
        self.assertEqual(r1, reservations[0])
        self.assertEqual(r2, reservations[2])
        self.assertEqual(r3, reservations[1])


