from django.test import TestCase
from ..models import Menu


class BookingTest(TestCase):
    def test_get_item(self):
        sut = Menu.objects.create(
            title='test booking title', price=20.55, inventory=1)
        self.assertEqual(str(sut), "test booking title : $20.55")
