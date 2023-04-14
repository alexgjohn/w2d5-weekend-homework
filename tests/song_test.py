import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):

        self.song1 = Song("Without Me", "Eminem", "Rap")
        self.song2 = Song("Song 2", "Blur", "BritPop")

    def test_song_has_name(self):
        result = self.song1.get_song_name()
        self.assertEqual("Without Me", result)

    def test_song_has_artist(self):
        result = self.song2.get_song_artist()
        self.assertEqual("Blur", result)

    def test_song_has_genre(self):
        result = self.song1.get_song_genre()
        self.assertEqual("Rap", result)

