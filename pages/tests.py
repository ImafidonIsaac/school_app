from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)

	def test_homepage_url_name(self):
		response = self.client.get(reverse("pages:home"))
		self.assertEqual(response.status_code, 200)