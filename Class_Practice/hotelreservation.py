# Hotel Reservation Project

#  TODO: Create Room class
class HotelRoom(object):

    def __init__(self):
        pass
    @property
    def price(self):
        return self._price

    @property
    def availability(self):
        self._availability = None
        return self._availability

    @availability.setter
    def availability(self, val):
        val = self.book_room
        return val

    @property
    def room_info(self):
        return self._room_info

    @property
    def book_room(self):
        self.availability = False
        return self.availability


class Penthouse(HotelRoom):

    def __init__(self):
        super().__init__()
        pass

    @HotelRoom.price.setter
    def price(self, val):
        #val = 350
        self._price = val
        return self._price

hotel_room = HotelRoom()
print(hotel_room.price)
my_room = Penthouse()
print(my_room.price)
my_room.price = 350
print(my_room.price)
print(my_room.availability)


# TODO: Create subroom classes like (1 bed room, 2 bed room, king suite, penthouse)
# TODO: Be able to search for room availability, price etc.
