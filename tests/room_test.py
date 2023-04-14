import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.guest1 = Guest("Bob", 20, ["Rock", "Rap"])
        self.guest2 = Guest("Jade", 200, ["Dance"])
        self.guest3 = Guest("Toby", 10, ["Classical"])
        self.song1 = Song("Without Me", "Eminem", "Rap")
        self.song2 = Song("Song 2", "Blur", "BritPop")
        self.ruby_songs = []
        self.emerald_songs = []
        self.diamond_songs = []
        self.room1 = Room("Ruby Room", 3, 5, self.ruby_songs)
        self.room2 = Room("Emerald Room", 10, 5, self.emerald_songs)
        self.room3 = Room("Diamond Room", 12, 10, self.diamond_songs)

    def test_room_has_name(self):
        result = self.room1.get_room_name()
        self.assertEqual("Ruby Room", result)

    def test_room_has_capacity(self):
        result = self.room2.get_room_capacity()
        self.assertEqual(10, result)

    def test_room_has_entree_fee(self):
        result = self.room1.get_room_entree_fee()
        self.assertEqual(5, result)

    def test_room_has_songs__no(self):
        result = len(self.room2.songs)
        self.assertEqual(0, result)

    def test_room_has_songs__yes(self):
        self.room3.songs.append(self.song1)
        self.room3.songs.append(self.song2)
        result = len(self.room3.songs)
        self.assertEqual(2, result)

    def test_room_can_add_songs(self):
        self.room1.add_song_to_room(self.song1)
        result = len(self.room1.songs)
        self.assertEqual(1, result)

    def test_room_can_remove_songs(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        self.room1.remove_song_from_room(self.song2)
        result = len(self.room1.songs)
        self.assertEqual(1, result)

    def test_room_can_add_guests(self):
        result = len(self.room1.guests)
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        result = len(self.room1.guests)
        self.assertEqual(2, result)

    def test_room_can_remove_guests(self):
        self.room2.check_in(self.guest1)
        self.room2.check_in(self.guest2)
        self.room2.check_out(self.guest1)
        result = len(self.room2.guests)
        self.assertEqual(1, result)

    def test_room_is_full__no(self):
        result = self.room2.room_is_full()
        self.assertEqual(False, result)

    def test_room_is_full__yes(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        result = self.room1.room_is_full()
        self.assertEqual(True, result)

    
