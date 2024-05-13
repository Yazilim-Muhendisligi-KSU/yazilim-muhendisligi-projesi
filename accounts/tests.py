from django.test import TestCase
from . import models



class WhatchedStockTest(TestCase):
    def setUp(self):
        models.WatchedStock.objects.create(user=models.User.objects.get(username="admin"), stock_symbol="EGSER")

    def test_WatchedStock(self):
        watched_stock = models.WatchedStock.objects.get(user=models.User.objects.get(username="admin"))
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')