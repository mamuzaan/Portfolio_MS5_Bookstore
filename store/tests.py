from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('store:store')

    def test_index_view(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'store/index.html')
