#Fourth assignment
"""
This loop will run 10 times,
the last number that will be printed is 10
"""

#Fifth assignment
my_age = 28
first_letter_of_last_name = 'G'
current_shekel_dollar_currency = 0.28
did_i_flew_aboard = True
my_apartment_number = 7

print(f"\n My age is: {my_age}\n"
      f" The first letter of my last name is: {first_letter_of_last_name}\n"
      f" The current Shekel to Dollar currency is: {current_shekel_dollar_currency}\n"
      f" Is it true that I flew aboard? {did_i_flew_aboard}\n"
      f" what is my apartment number? {my_apartment_number}\n")


def adding_age_and_currency (age, currency):
    summit = age + currency
    return summit


summit = adding_age_and_currency(my_age, current_shekel_dollar_currency)
print(summit)
