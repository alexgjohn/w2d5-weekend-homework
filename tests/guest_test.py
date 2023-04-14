import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.guest1 = Guest("Tyler", 100, ["Rock", "Rap", "Metal"])
        self.guest2 = Guest("Sofia", 50, ["Pop", "Dance"])
        self.guest3 = Guest("Bryce", 80, ["BritPop", "Disco", "Jazz"])

    def test_guest_has_name(self):
        result = self.guest1.get_guest_name()
        self.assertEqual("Tyler", result)

    def test_guest_has_wallet(self):
        result = self.guest2.get_guest_wallet()
        self.assertEqual(50, result)

    def test_guest_has_favourite_genres(self):
        result = len(self.guest3.favourite_genres)
        self.assertEqual(3, result)