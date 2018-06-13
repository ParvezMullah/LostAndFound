from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from .models import LostAndFound
# Create your tests here.

class LostAndFountTestCase(TestCase):
    title = 'a new title'
    def setUp(self):
        LostAndFound.objects.create(lost_or_found = 'lost', title = self.title)

    def test_lostandfound_lost_or_found(self):
        lostandfound = LostAndFound.objects.get(title = self.title)
        self.assertEqual('lost', lostandfound.lost_or_found)
        self.assertEqual(slugify(self.title), lostandfound.slug)
