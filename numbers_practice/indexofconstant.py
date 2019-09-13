import math

def get_nth_place(constant, string_constant):
    nth_place = input("Please enter what nth place you would like the constant %s to: " % string_constant)
    formatted_nth_place = '.' + nth_place + 'f'
    print((format(constant, formatted_nth_place)))

def fibonacci_seq():
    nth_place = int(input("Please enter what number you would like the Fibonacci sequence to: "))
    for idx, num in enumerate(range(nth_place + 1)):
        if idx < 2:
            num_list.append(num)
            continue
        else:
            math = num_list[idx - 1] + num_list[idx - 2]
            num_list.append(math)
    print(num_list)

pi = math.pi
get_nth_place(pi, 'pi')

e = math.e
get_nth_place(e, 'e')

num_list = []
fibonacci_seq()
