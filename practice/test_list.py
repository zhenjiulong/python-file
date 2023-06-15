import unittest
from 练习.list import ShoppingList

class TestShoppingList(unittest.TestCase):
    def test_get_item_count(self):
        shoppinglist = ShoppingList({"纸巾":8,"帽子":30,"拖鞋":15})
        self.assertEqual(shoppinglist.get_item_count(),3)

    def test_get_total_price(self):
        shoppinglist = ShoppingList({"纸巾":8,"帽子":30,"拖鞋":15})
        self.assertEqual(shoppinglist.get_total_price(),53)
