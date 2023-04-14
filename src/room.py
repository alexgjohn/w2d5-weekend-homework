class Room:

    def __init__(self, input_name, input_capacity, input_entree_fee, input_songs):
        self.name = input_name
        self.capacity = input_capacity
        self.entree_fee = input_entree_fee
        self.songs = input_songs
        self.guests = []

    def get_room_name(self):
        return self.name
    
    def get_room_capacity(self):
        return self.capacity
    
    def get_room_entree_fee(self):
        return self.entree_fee
    
    def check_in(self, guest):
        if self.room_is_full() != True:
            self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)
    
    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)

    def room_is_full(self):
        return len(self.guests) >= self.capacity

    

    
