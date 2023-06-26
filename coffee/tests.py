from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Coffee
from django.http import HttpResponseRedirect


class CoffeeTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse("coffee_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("coffee_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "coffee/coffee-list.html")
        self.assertTemplateUsed(response, "_base.html")

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", email="test@example.com", password="1234"
        )

        self.coffee = Coffee.objects.create(
            name="Test Coffee",
            price=10.99,
            desc="Test info",
            purchaser=self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.coffee), "Test Coffee")

    def test_detail_view(self):
        url = reverse("coffee_detail", args=[self.coffee.pk])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "coffee/coffee-detail.html")


