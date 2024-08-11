from django.test import TestCase
from restaurant.models import *

class MenuViewTest(TestCase):
	def test_get_item(self):
		return