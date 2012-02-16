from django.test import TestCase
from test_serenesiri.models import SereneModel


class TestSereneModel(TestCase):

    def setUp(self):
        self.serene = SereneModel.objects.create(name='Super Serene')

    def test_unicode(self):
        self.assertEqual(unicode(self.serene), 'Super Serene')