import unittest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):

        self.bar = KaraokeBar("Sing, Fools!")
        self.bar.drinks = [{"Beer" : 5},
                            {"Wine" : 4},
                            {"Champagne" : 15
                            }]
        self.guest1 = Guest("Bob", 20, ["Rock", "Rap"], "Song 2")
        self.guest2 = Guest("Jade", 200, ["Dance"], "Safety Dance")
        self.guest3 = Guest("Toby", 10, ["Classical"], "Beethoven's 9th Symphony")
        self.song1 = Song("Without Me", "Eminem", "Rap")
        self.song2 = Song("Song 2", "Blur", "BritPop")
        self.ruby_songs = []
        self.emerald_songs = []
        self.diamond_songs = []
        self.room1 = Room("Ruby Room", 3, 5, self.ruby_songs)
        self.room2 = Room("Emerald Room", 10, 5, self.emerald_songs)
        self.room3 = Room("Diamond Room", 12, 20, self.diamond_songs)
        self.bar.rooms = [self.room1, self.room2]


    def test_karaoke_bar_has_name(self):
        result = self.bar.name
        self.assertEqual("Sing, Fools!", result)

    def test_karaoke_bar_has_rooms(self):
        result = len(self.bar.rooms)
        self.assertEqual(2, result)

    def test_karaoke_bar_has_drinks(self):
        result = len(self.bar.drinks)
        self.assertEqual(3, result)

    def test_karaoke_bar_has_cash(self):
        result = self.bar.total_cash
        self.assertEqual(0, result)

    def test_karaoke_bar_can_change_name(self):
        self.bar.name = "Keep Singing!"
        result = self.bar.name
        self.assertEqual("Keep Singing!", result)

    def test_karaoke_bar_can_add_new_room(self):
        self.bar.add_new_room(self.room3)
        result = len(self.bar.rooms)
        self.assertEqual(3, result)

    def test_karaoke_bar_can_add_drink(self):
        self.bar.add_drink({"Cocktail" : 20})
        result = len(self.bar.drinks)
        self.assertEqual(4, result)

    def test_karaoke_bar_can_increase_cash(self):
        self.bar.increase_cash(50)
        result = self.bar.total_cash
        self.assertEqual(50, result)

    def test_karaoke_bar_can_add_guests_to_bar(self):
        self.bar.add_guest_to_bar(self.guest1)
        self.bar.add_guest_to_bar(self.guest2)
        result = len(self.bar.guests_at_bar)
        self.assertEqual(2, result)

    def test_get_total_guests(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.bar.add_guest_to_bar(self.guest3)
        result = self.bar.get_total_number_of_guests()
        self.assertEqual(3, result)

    