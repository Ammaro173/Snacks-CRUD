from django.test import TestCase

# Create your tests here.

from django.urls import reverse


class SnackTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")
