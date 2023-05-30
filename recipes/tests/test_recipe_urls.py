from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipes_url_home(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipes_url_category(self):
        url = reverse('recipes:category', kwargs={"category_id": 1})
        self.assertEqual(url, "/recipes/category/1/")

    def test_recipes_url_recipe(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')
