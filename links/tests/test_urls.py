from django.test import SimpleTestCase
from django.urls import reverse, resolve
from links.views import LinksListView


class TestUrls(SimpleTestCase):

    def test_index_url_resolved(self):

        url = reverse('links:links')

        self.assertEqual(resolve(url).func.view_class, LinksListView)