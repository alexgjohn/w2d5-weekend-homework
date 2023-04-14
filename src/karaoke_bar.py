class KaraokeBar:

    def __init__(self, input_name):
        self.name = input_name
        self.rooms = []
        self.drinks = []
        self.guests_at_bar = []
        self.total_cash = 0

    def add_new_room(self, new_room):
        self.rooms.append(new_room)

    def add_drink(self, new_drink):
        self.drinks.append(new_drink)

    def increase_cash(self, amount):
        self.total_cash += amount

    def add_guest_to_bar(self, new_guest):
        self.guests_at_bar.append(new_guest)

    def get_total_number_of_guests(self):
        total_guests = 0
        total_guests += len(self.guests_at_bar)
        for room in self.rooms:
            total_guests += len(room.guests)
        return total_guests