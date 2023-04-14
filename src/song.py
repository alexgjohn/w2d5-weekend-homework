class Song:

    def __init__(self, input_name, input_artist, input_genre):
        self.name = input_name
        self.artist = input_artist
        self.genre = input_genre

    
    def get_song_name(self):
        return self.name
    
    def get_song_artist(self):
        return self.artist
    
    def get_song_genre(self):
        return self.genre
    
    