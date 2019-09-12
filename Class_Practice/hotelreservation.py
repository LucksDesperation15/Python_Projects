# Hotel Reservation Project
import datetime as dt
import random

# Create Room class
class Hotel(object):

    def __init__(self):
        self._price = 0
        self._room_info = None
        self._availability = None

# Create subroom classes like (1 bed room, 2 bed room, king suite, penthouse)

class Penthouse(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 650
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

class King(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 350
        self._room_info =('''
-550 sq. ft. / 51 sq. m.
-One king bed
-Located on floors 5 - 19
-Overlooks interior courtyard or 58th Street
-Large wood-paneled luxury closets with built-in drawers and storage
-Bathroom features beautiful mosaic floors and walls with a gilded floral motif, private WC, and 24-carat gold-plated fixtures.
-Most feature a soaking tub and separate shower
-Deluxe King Rooms accommodate a rollaway bed
-White glove butler service upon request
        ''')
        self._availability = True


class Queen(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 250
        self._room_info =('''
-Open plan suite with sitting area and full size sofa bed
-Can accommodate up to 6 people
-On floors 12 - 18
-Two queen beds
-Large wood-paneled luxury closets with built-in drawers and storage
-Bathroom features beautiful mosaic floors and walls with a gilded floral motif, private WC, and 24-carat gold-plated fixtures
-Soaking tub and separate shower
-Marble wet bar
-Family Grand Luxe Two Queens can accommodate a rollaway bed
-White glove butler service
        ''')
        self._availability = True

class Double(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 200
        self._room_info =('''
-550 sq. ft. / 51 sq. m.
-Two queen beds
-Overlooks 58th street
-Located on floors 5 - 10
-Large wood-paneled luxury closets with built-in drawers and storage
-Bathroom features beautiful mosaic floors and walls with a gilded floral motif, private WC, and 24-carat gold-plated fixtures
-White glove butler service upon request
        ''')
        self._availability = True

class Single(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 100
        self._room_info =('''
-550 sq. ft. / 51 sq. m.
-One queen bed
-Overlooks 58th street
-Located on floors 5 - 10
-Large wood-paneled luxury closets with built-in drawers and storage
-Bathroom features beautiful mosaic floors and walls with a gilded floral motif, private WC, and 24-carat gold-plated fixtures
-White glove butler service upon request
        ''')
        self._availability = True

class Broom_Closet(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 35
        self._room_info =('''
-55 sq. ft.
-One cot
-Views of a dark and dingy wall
-Located on floors 5 - 10
-Small bag for storage
-Tin bucket supplied for all bathroom needs
-Will clean room when we remember
        ''')
        self._availability = True


def test():
    penthouse = Penthouse()
    king = King()
    queen = Queen()
    double = Double()
    single = Single()
    broom_closet = Broom_Closet()
    print(f'''Penthouse:\nPrice:${penthouse.price}\n\nInfo:{penthouse.room_info}
Availability:{penthouse.availability}
    ''')
    print('-' * 50)
    print(f'''King:\nPrice:${king.price}\n\nInfo:{king.room_info}
Availability:{king.availability}
    ''')
    print('-' * 50)

    print(f'''Queen:\nPrice:${queen.price}\n\nInfo:{queen.room_info}
Availability:{queen.availability}
    ''')
    print('-' * 50)

    print(f'''Double:\nPrice:${double.price}\n\nInfo:{double.room_info}
Availability:{double.availability}
    ''')
    print('-' * 50)

    print(f'''Single:\nPrice:${single.price}\n\nInfo:{single.room_info}
Availability:{single.availability}
    ''')
    print('-' * 50)

    print(f'''Broom Closet:\nPrice:${broom_closet.price}\n\nInfo:{broom_closet.room_info}
Availability:{broom_closet.availability}
    ''')
    print('-' * 50)

#test()

# TODO: Be able to book the room for the dates the customer wants

check_in = '12/1/2019'
check_out = '12/6/2019'

print("Hello! Welcome to the Plaza NYC. Please enter your check-in and check-out days: ")

def date_validation(check_in_or_out, in_or_out):
    while True:
        try:
            valid_date = dt.datetime.strptime(check_in_or_out,'%m/%d/%Y')
            break
        except ValueError:
            print('Invalid date range. Please try again by entering the following format: (mm/dd/yyyy)')
            check_in_or_out = input(f'Check-{in_or_out} (mm/dd/yyyy)>> ')
            continue

def format_dates(date):
    month_day_year_list =  date.split('/')
    month = month_day_year_list[0]
    day = month_day_year_list[1]
    year = month_day_year_list[2]
    year_month_day_list = [year, month, day]
    formatted_date = '-'.join(year_month_day_list)
    return formatted_date

def room_type_string_validation(string, string_choice_list, user_string):
    while True:
        if string in string_choice_list:
            return string.title()
            break
        else:
            print('Invalid entry.')
            string = input(f'{user_string}')



def confirmation_string_validation(string):
    while True:
        if string.upper() in ['Y','N','YES','NO'] or string == '':
            return string
            break
        else:
            print('Please enter either Y or N.')
            string = input('Enter Y to confirm or N to change your dates: ')
            continue

def check_in_or_out_confirmation(confirmation):
    pass

# TODO: Create list of rooms that are available to stay at in the hotel.
# This should be an attribute of the hotel. I should create in the beginning.
room_list = {
'Penthouse' : [5, Penthouse()],
'King' : [20, King()],
'Queen' : [40, Queen()],
'Double' : [40, Double()],
'Single' : [10, Single()],
'Broom Closet' : [1, Broom_Closet()]
}


# Commented out for testing. UNCOMMENT WHEN ENTERING PRODUCTION!!!!!!!
'''
check_in = input('Check-in (mm/dd/yyyy)>> ')
date_validation(check_in, 'in')
check_out = input('Check-out (mm/dd/yyyy)>> ')
date_validation(check_out, 'out')
'''

date_check_in = dt.datetime.strptime(format_dates(check_in), '%Y-%m-%d').date()
print(date_check_in)
date_check_out = dt.datetime.strptime(format_dates(check_out), '%Y-%m-%d').date()
print(date_check_out)

print(f'''So you would like to check in on {check_in} and check out on {check_out}
for a total of {(date_check_out - date_check_in).days} nights. Is this correct?
''')
confirmation = input('Enter Y to confirm or N to change your dates: ')
valid_confirmation = confirmation_string_validation(confirmation)
if valid_confirmation.upper() in ['N','NO']:
    check_in = input('Please enter your new check-in date (mm/dd/yyyy)>> ')
    date_validation(check_in, 'in')
    check_out = input('Please enter your new check-out date (mm/dd/yyyy)>> ')
    date_validation(check_out, 'out')

# TODO: Now that dates are confirmed let the customer know
# what rooms are available.
for room in room_list:
    print(f'''
{room}:
Room(s) available: {room_list[room][0]}
Price per night: ${room_list[room][1].price}
    ''')
room_type_string = 'Which room would you like to book? >> '
room_type_list = room_list.keys()
room_type = input(f'{room_type_string}')
user_room_type = room_type_string_validation(room_type, room_type_list, room_type_string)

print(f'A {user_room_type} room has been booked. Your room number is {random.randint(0,51)}')
room_list[user_room_type] = room_list[user_room_type][0] - 1

# Think I will end the code here as I feel I am venturing out of
# practicing classes. Did not add the ability to book certain dates
# as that is just writing a conditional statement using datetime
