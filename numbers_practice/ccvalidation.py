# Credit Card validation/Luhn's Algorithim
# Valid number: 79927398713
# NOT a Valid number: 51237894265

credit_card_num = 79927398713


reverse_credit_card_lst = []
for num in str(credit_card_num)[::-1]:
    reverse_credit_card_lst.append(num)

final_check_digits = []
for idx, check_nums in enumerate(reverse_credit_card_lst):
    if idx % 2 == 0:
        final_check_digits.append(int(check_nums))
    else:
        check_nums_test = int(check_nums) * 2
        if check_nums_test > 9:
            check_nums_test_lst = list(map(int,str(check_nums_test)))
            check_nums_final_result = int(check_nums_test_lst[0]) + int(check_nums_test_lst[1])
            final_check_digits.append(check_nums_final_result)
        else:
            final_check_digits.append(check_nums_test)
            continue

sum_final_check_digits = sum(final_check_digits)

if sum_final_check_digits % 10 == 0:
    print("This is a valid Credit Card number")
else:
    print("This is NOT a valid Credit Card number")
