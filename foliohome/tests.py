from django.test import TestCase
from django.urls import reverse

class TestHomePage(TestCase):
    def test_admin_status_code(self):
        url = reverse('admin:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)