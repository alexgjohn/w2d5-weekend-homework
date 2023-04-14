class Guest:

    def __init__(self, input_name, input_wallet, input_favourite_genres, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_genres = input_favourite_genres
        self.favourite_song = input_favourite_song

    def get_guest_name(self):
        return self.name
    
    def get_guest_wallet(self):
        return self.wallet
    
    def get_guest_favourite_genres(self):
        return self.favourite_genres
    
    def get_guest_favourite_song(self):
        return self.favourite_song