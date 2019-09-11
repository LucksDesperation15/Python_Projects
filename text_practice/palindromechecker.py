# Palindrome checker

def string_validation(string, string_instruction):
    while True:
        if string.replace(' ','').lower().isalpha():
            if string.replace(' ','').lower()[::-1] == string.replace(' ','').lower():
                print("The word you entered is a Palindrome!")
                string = input("Please enter another word. If you're done please hit enter. >>")
                if string == '':
                    break
                else:
                    continue
            else:
                print("The word you entered is NOT a Palindrome!")
                string = input("Please enter another word. If you're done please hit enter. >>")
                if string == '':
                    break
                else:
                    continue
            break
        else:
            print('Please enter a valid input.')
            string = input(f'{string_instruction}')

string_instruction = 'Please enter a word to see if it is a Palindrome. >> '
user_input = input(f'{string_instruction}')
string_validation(user_input, string_instruction)
