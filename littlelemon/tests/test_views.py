from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self): 
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="IceCream", price=8, inventory=100)
        self.item2 = Menu.objects.create(title="Brownies", price=5, inventory=90)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/') 
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)