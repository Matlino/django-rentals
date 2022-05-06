from django.test import TestCase
from django.urls import reverse


class RentalListTest(TestCase):

    def test_status_code(self):
        url = reverse('rentals')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

