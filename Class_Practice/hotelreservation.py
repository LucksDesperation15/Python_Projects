# Hotel Reservation Project
import datetime as dt
# Create Room class
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

        ''')
        self._availability = True


class Queen(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 250
        self._room_info =('''

        ''')
        self._availability = True

class Double(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 200
        self._room_info =('''

        ''')
        self._availability = True

class Single(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 100
        self._room_info =('''

        ''')
        self._availability = True

class Broom_Closet(HotelRoom):

    def __init__(self):
        super().__init__()
        self._price = 35
        self._room_info =('''

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
For a total of {(date_check_out - date_check_in).days} days. Is this correct?
''')
confirmation = input('Enter Y to confirm or N to change your dates: ')


# TODO: Maybe have a sort of front desk usability for an employee
# to make a booking for someone over the phone
