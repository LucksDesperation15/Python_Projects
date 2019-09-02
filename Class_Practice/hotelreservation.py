# Hotel Reservation Project

# TODO: Create Room class
class HotelRoom(object):

    def __init__(self):
        self._price = 0
        self._room_info = None
        self._availability = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        self._price = val
        return self._price

    @property
    def room_info(self):
        return self._room_info

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, val):
        self._availability = val
        return self._availability
'''
    @availability.setter
    def availability(self, val):
        val = self.book_room
        return val
'''

'''
    @property
    def book_room(self):
        self.availability = False
        return self.availability
'''

class Penthouse(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 350
        self._room_info =('''
-One bedroom suite plus separate parlor room
-1000 sq. ft. / 93 sq. m.
-Partial views of Central Park
-One suite per floor on floors 11 - 19
-One king bed and one full size sofa bed
-Large wood-paneled luxury closets with built-in drawers and storage
-Bathroom features beautiful mosaic floors and walls with a gilded floral motif, private WC, and 24-carat gold-plated fixtures
-Soaking tub and separate shower
-Separate powder room
-Marble wet bar
-White glove butler service
        ''')
        self._availability = True


hotel_room = HotelRoom()
#print(hotel_room._price)
print(hotel_room.price)
my_room = Penthouse()
print(my_room.price)
my_room.price = 450
print(my_room.price)
print(my_room.room_info)
print(my_room.availability)
my_room.availability = False
print(my_room.availability)


# TODO: Create subroom classes like (1 bed room, 2 bed room, king suite, penthouse)
# TODO: Be able to search for room availability, price etc.
