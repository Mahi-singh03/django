from django.test import TestCase
from restaurant.models import *

class MenuModelTest(TestCase):
	def test_get_item(self):
		item = Menu.objects.create(title="Ice Cream", price=8, inventory=100)
		self.assertEqual(str(item), "Ice Cream: 8")