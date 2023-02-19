from django.test import TestCase, RequestFactory
from ..models import Menu
from ..serializers import MenuSerializer
from ..views import MenuItemView

test_data = [
    {
        'title': 'first title',
        'price': 10.99,
        'inventory': 2,
    },
    {
        'title': 'second title',
        'price': 4.55,
        'inventory': 4,
    }
]


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        for data in test_data:
            Menu.objects.create(
                title=data["title"],
                price=data["price"],
                inventory=data["inventory"],
            )

    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        request = self.factory.get('/restaurant/menu/')
        response = MenuItemView.as_view()(request)

        self.assertEqual(response.data, serialized_items.data)
