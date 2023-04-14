class Guest:

    def __init__(self, input_name, input_wallet, input_favourite_genres):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_genres = input_favourite_genres

    def get_guest_name(self):
        return self.name
    
    def get_guest_wallet(self):
        return self.wallet
    
    def get_guest_favourite_genres(self):
        return self.favourite_genres