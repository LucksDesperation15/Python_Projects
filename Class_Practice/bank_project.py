# Create a bank program that can keep track of pretend accounts.

# The bank should be able to store multiple accounts using some ytpe of randomized ID.
# It should be able to check that this account does not already exist.

# Each account should have a balance where you can either withdraw or deposit money into it.
# You should receive a warning when you are about to draw more than you have in your account.

import random as rand

# !!! Might be an issue to use a set as it doesn't have any indication to the customer info.

# !!! Perhaps create a customer number as well and then a dic that has customer number

# !!! as the key and then account number as value?

# Where all the account and customer information is held.

class Bank:

    def __init__(self):

        self.accountset = set()
        self.current_account = None
        self.accountdic = {}
        self.introduction()
        self.show_options()

    def introduction(self):
        print('Welcome to The Bank!')
        print('Please select from the options below: ')

    # EFFECTS: Displays options for the user to pick with numbers.
    def show_options(self):
        print(' 1. Make a Deposit')
        print(' 2. Make a Withdrawal')
        print(' 3. Speak to a teller')
        print(' 4. Display balance')
        print(' 5. Create Account')
        print(' 6. Exit')

    # EFFECTS: Creates a loop that allows the user to perform a number of actions until option 6 is chosen.
    def home_page(self, user_input):
        self.user_input = user_input

        while self.user_input != 6:
            self.user_selection(self.user_input)
            self.show_options()
            self.user_input = self.get_user_input()

    # REQUIRES: Integer
    # MODIFIES: self.accountset, self.current_account, current_account.balance
    # EFFECTS: Asks user to type a number to begin an action for the option they chose.
    def user_selection(self, user_choice):
        self.user_choice = user_choice
        if self.user_choice == 1:
            if len(self.accountset) < 1:
                print("It appears you don't have an account please create one.")
            else:
                print('You chose make a deposit.')
                deposit_amt = self.get_deposit_info()
                self.current_account.make_deposit(deposit_amt)
                print(deposit_amt)

        elif self.user_choice == 2:
            if len(self.accountset) < 1:
                print("It appears you don't have an account please create one.")
            else:
                print('You chose make a withdrawal.')
                withdrawal_amt = self.get_withdrawal_info()
                self.current_account.make_withdrawl(withdrawal_amt)
                print(withdrawal_amt)

        elif self.user_choice == 3:
            print('You chose talk to a teller.')
            print('Hello I\'m a teller look at me!')

        elif self.user_choice == 4:
            if self.current_account == None:
                print("It appears you don't have an account please create one.")
            else:
                print('You chose make a display balance.')
                print(self.current_account.balance)

        elif self.user_choice == 5:
            self.create_account()
        else:
            # This will require account information to be stored in some type of db more than likely SQL.
            # retrieve_account()
            pass

    # EFFECTS: Gets an amount for deposit from the user and returns it.
    def get_deposit_info(self):
        print('How much would you like to deposit?')
        deposit_amt = input('>>$')
        if check_if_integer(deposit_amt) == False:
            return self.get_deposit_info()
        print(f'You would like to deposit ${deposit_amt}. Is this correct?')
        user_confirmation = input('(Y/N)>> ')
        if user_confirmation.title() == 'Y' or user_confirmation.title() == 'Yes':
            return int(deposit_amt)
        else:
            return self.get_deposit_info()

    # EFFECTS: Gets an amount for withdrawal from the user and returns it.
    def get_withdrawal_info(self):
        print('How much would you like to withdraw?')
        withdrawal_amt = input('>>$')
        if check_if_integer(withdrawal_amt) == False:
            return self.get_withdrawal_info()
        print(f'You would like to deposit ${withdrawal_amt}. Is this correct?')
        user_confirmation = input('(Y/N)>> ')
        if user_confirmation.title() == 'Y' or user_confirmation.title() == 'Yes':
            return int(withdrawal_amt)
        else:
            return self.get_withdrawal_info()

    # EFFECTS: Gets the users input and takes the first character from the input.
    def get_user_input(self):
        user_input = input('>> ')
        if check_if_integer(user_input) == False:
            self.show_options()
            return self.get_user_input()
        user_choice = int(user_input[0])
        return user_choice

    # MODIFIES: self.accountdic, self.accountset, self.current_account.
    # EFFECTS: Creates a random 9 digit number within the below range and prints it to the screen
    def create_account(self):
        new_account_number = rand.randint(100000000, 999999999)
        new_account = Account()
        self.accountdic[new_account] = new_account_number
        self.accountset.add(new_account_number)
        print('A new account has been created please find your account number below: ')
        print(new_account_number)
        self.current_account = new_account

    def retrieve_account(self):
        pass

# Customer should have their own unique account at the bank.
# If they don't have one give them a new one.

class Customer:

    def __init__(self):
        pass

# An account should have a balance(always) where one who is a customer at the bank
# can take certain actions such as withdrawing and depositing.

class Account:

    # EFFECTS: Creates the balance for the Account.
    def __init__(self):
        self.balance = 0
        pass

    # REQUIRES: Integer
    # MODIFIES: self.balance
    # EFFECTS: Takes amt from arg and adds it to the current balance for the account.
    def make_deposit(self, amt):
        self.amt = amt
        print('Deposit made!')
        self.balance += self.amt

    # REQUIRES: Integer
    # MODIFIES: self.balance
    # EFFECTS: Takes amt from arg and subtracts it from the current balance for the account.
    def make_withdrawl(self, amt):
        self.amt = amt
        print('Withdraw made!')
        self.balance -= self.amt

    # EFFECTS: prints the current balance for the account.
    def show_balance(self):
        print(self.balance)

# REQUIRES: String
# EFFECTS: Checks to see if what the user entered was an integer and not a string.
def check_if_integer(user_input):
    try:
        int(user_input)
        return True
    except:
        print('Invalid entry. Please enter a number.')
        return False

class Test:
    def __init__(self):
        test_bank_1 = Bank()
        second_acc_num = test_bank_1.create_account()
        pass

    def test_if_in_set(self, acc_num_1):
        pass

x = Bank()
initial_user_input = x.get_user_input()
x.home_page(initial_user_input)
# print(x.accountset)
# t = Test()
