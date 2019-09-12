# Mortgage Calculator

principal = int(input('How much is your principal amount?: '))
rate = int(input('What is the interest rate you borrowed at?: '))
decimal_rate = rate / 100
monthly_decimal_rate = decimal_rate / 12
years = int(input('Finally how many years is the loan for?: '))
num_of_pmts_yearly = years
num_of_pmts_monthly = years * 12

monthly_pmt_numerator = (monthly_decimal_rate*(1 + monthly_decimal_rate)**num_of_pmts_monthly)
monthly_pmt_denominator = (((1 + monthly_decimal_rate)**num_of_pmts_monthly) - 1)
monthy_pmt = round(principal * (monthly_pmt_numerator/monthly_pmt_denominator))
print('Your monthly payment is ${}'.format(monthy_pmt))
