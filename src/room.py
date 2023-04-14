class Room:

    def __init__(self, input_name, input_capacity, input_entry_fee, input_songs):
        self.name = input_name
        self.capacity = input_capacity
        self.entry_fee = input_entry_fee
        self.songs = input_songs
        self.guests = []
        self.cash_taken = 0

    def get_room_name(self):
        return self.name
    
    def get_room_capacity(self):
        return self.capacity
    
    def get_room_entry_fee(self):
        return self.entry_fee
    
    def check_in(self, guest):
        if self.room_is_full() != True and guest.wallet >= self.entry_fee:
            self.guests.append(guest)
            guest.wallet -= self.entry_fee
            self.cash_taken += self.entry_fee

    def check_out(self, guest):
        self.guests.remove(guest)
    
    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)

    def room_is_full(self):
        return len(self.guests) >= self.capacity

    def guest_likes_song(self, song_playing):
        if song_playing in self.songs:
            for guest in self.guests:
                return f"Whoo! {guest.name} likes this song!"
            
    def guest_loves_song(self, song_playing):
        if song_playing in self.songs:
            for guest in self.guests:
                return f"Whoo! This is {guest.name}'s favourite song!"
        


    
