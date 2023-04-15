import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.guest1 = Guest("Bob", 40, 20, ["Rock", "Rap"], "Song 2")
        self.guest2 = Guest("Jade", 17, 200, ["Dance"], "Safety Dance")
        self.guest3 = Guest("Toby", 28, 10, ["Classical"], "Beethoven's 9th Symphony")
        self.song1 = Song("Without Me", "Eminem", "Rap")
        self.song2 = Song("Song 2", "Blur", "BritPop")
        self.ruby_songs = []
        self.emerald_songs = []
        self.diamond_songs = []
        self.room1 = Room("Ruby Room", 3, 5, self.ruby_songs)
        self.room2 = Room("Emerald Room", 10, 5, self.emerald_songs)
        self.room3 = Room("Diamond Room", 12, 20, self.diamond_songs)

    def test_room_has_name(self):
        result = self.room1.get_room_name()
        self.assertEqual("Ruby Room", result)

    def test_room_has_capacity(self):
        result = self.room2.get_room_capacity()
        self.assertEqual(10, result)

    def test_room_has_entry_fee(self):
        result = self.room1.get_room_entry_fee()
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
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.assertEqual(2, len(self.room1.guests))
        self.assertEqual(15, self.guest1.wallet)
        self.assertEqual(10, self.room1.cash_taken)

    def test_room_can_remove_guests(self):
        self.room2.check_in(self.guest1)
        self.room2.check_in(self.guest2)
        self.room2.check_out(self.guest1)
        result = len(self.room2.guests)
        self.assertEqual(1, result)
    
    def test_guest_cannot_afford_room(self):
        self.room3.check_in(self.guest3)
        result = len(self.room3.guests)
        self.assertEqual(0, result)

    def test_room_is_full__no(self):
        result = self.room2.room_is_full()
        self.assertEqual(False, result)

    def test_room_is_full__yes(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        result = self.room1.room_is_full()
        self.assertEqual(True, result)

    def test_guest_likes_song_in_room(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        result = self.room1.guest_likes_song(self.song1)
        self.assertEqual("Whoo! Bob likes this song!", result)

    def test_guest_loves_song_in_room(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        result = self.room1.guest_loves_song(self.song2)
        self.assertEqual("Whoo! This is Bob's favourite song!", result)
    
    def test_clear_room(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        self.room1.clear_room()
        result = len(self.room1.guests)
        self.assertEqual(0, result)