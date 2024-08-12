from django.test import TestCase

from rest_framework.test import APIClient

import json

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        menu_items_info = [
            {'title': 'Apple', 'price': 1.1, 'inventory': 50}
            , {'title': 'Fries', 'price': 4.2, 'inventory': 30}
            , {'title': 'Drumstick', 'price': 5.1, 'inventory': 40}
        ]

        for info in menu_items_info:
            new_menu = Menu(**info)
            new_menu.save()

        self.client = APIClient()

    def test_getall(self):
        all_items = Menu.objects.all()

        serializer_all_items = MenuSerializer(all_items, many=True)
        
        resp = self.client.get('http://localhost:8000/restaurant/menu/')

        resp_content = resp.content.decode('utf-8')

        serialized_resp_content = json.loads(resp_content)
        
        self.assertEqual(serialized_resp_content, serializer_all_items.data)