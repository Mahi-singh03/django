from django.test import TestCase
import sys

from restaurant.models import Menu
#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # We cannot do this as defined from the assignment
        self.assertEqual(item.__str__(), "IceCream : 80")