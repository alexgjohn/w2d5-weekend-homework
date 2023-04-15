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
    
    def get_drink_price(self, drink_name):
        for drink in self.drinks:
            for key in drink:
                if key == drink_name:
                    return drink[drink_name]
            
    def guest_can_afford_drink(self, guest_buying, drink_name):
        price = self.get_drink_price(drink_name)
        return guest_buying.wallet >= price
    
    def guest_is_old_enough_to_drink(self, guest):
        return guest.age >= 18

    def sell_drink_to_guest(self, drink_sold, guest_buying):
        if self.guest_can_afford_drink(guest_buying, drink_sold) and self.guest_is_old_enough_to_drink:
            price = self.get_drink_price(drink_sold)
            guest_buying.wallet -= price
            self.total_cash += price

    def transfer_room_cash_to_total(self, room):
        self.total_cash += room.cash_taken
        room.cash_taken -= room.cash_taken

    def clear_guests_from_bar(self):
        self.guests_at_bar.clear()

    def end_of_night(self):
        for room in self.rooms:
            self.transfer_room_cash_to_total(room)
            room.clear_room()
        self.clear_guests_from_bar()