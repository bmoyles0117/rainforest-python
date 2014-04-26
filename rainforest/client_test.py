from .client import Rainforest
from unittest import TestCase

class TestRainforest(TestCase):
	def test_init(self):
		rainforest = Rainforest('CLIENT_TOKEN')

		self.assertEqual(rainforest.client_token, 'CLIENT_TOKEN')