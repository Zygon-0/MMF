import time
import pandas

# imports function that checks integers with a question minimum num maximum num and exit code
from _Functions.A_int_checker_v2 import int_check

# imports function that prints instructions
from _Functions.B_instructions import instructions

# imports function that decorates chosen text with chosen symbol(s) all around, just on the sides or sides and bottom
from _Functions.C_statement_generator_v3 import statement_generator

# imports function that checks a simple decision with a question, list of valid inputs and a customisable error message
from _Functions.D_choice_checker import choice_checker, yes_no_list

# imports function that checks floats with a question boundary's and an exit code
from _Functions.E_float_checker import float_check

# imports function that processes any sting with the addition of an exit variable
from _Functions.F_string_checker import string_checker

# imports currency formatter
from _Functions.G_currency import currency

# Defines default variable values
max_tickets = 5
tickets_sold = 0

pay_list = ["credit", "cash"]
c_c_list = ["1", "2"]

# lists to hold tickets data
# dictionaries to hold ticket details
all_names = []
all_tickets_costs = []
all_surcharge = []

# dictionary used to create data frame ie column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket price": all_tickets_costs,
    "Surcharge": all_surcharge
}

statement_generator("Mini Movie Fundraiser", "*#", 3)
print()

# asks if user wants instructions
yn_instructions = choice_checker("Would you like instructions: ", yes_no_list, "Please respond with yes or no", 1)

# prints the instructions if the user wants them
if yn_instructions == "yes":
    instructions()
else:
    print()

# looping component
while tickets_sold < 4:

    print("--------------------------------------------------")
    print()

    # gets users name
    user_name = string_checker("What is your name: ", "xxx")

    if user_name == "xxx":
        break

    print()
    user_age = int_check("What is your age: ")
    if 12 <= user_age <= 120:
        tickets_sold += 1
        print()
    elif user_age < 12:
        print("you are too young!")
        print()
        continue
    else:
        print("oops - that looks like a typo (too old)")
        print()
        continue

    if int(user_age) < 16:
        ticket_price = 7.50
    elif int(user_age) > 64:
        ticket_price = 6.50
    else:
        ticket_price = 10.50

    print(f"your ticket comes to a total of ${ticket_price:.2f}")

    pay_type = choice_checker("How would you like to pay(cash or credit): ", pay_list, "please enter ether cash or "
                                                                                       "credit(or the first 2 letters"
                                                                                       " of your choice)", 2)

    print(f"you chose to pay by {pay_type}")

    if pay_type == "cash":
        surcharge = 0
    else:
        surcharge = ticket_price * 0.05

    all_names.append(user_name)
    all_tickets_costs.append(ticket_price)
    all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')

# calculate the total cost (ticket = surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket price']
# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# currency formatting
add_dollars = ['Ticket price', 'Surcharge', 'Total', 'Profit']
for item in add_dollars:
    mini_movie_frame[item] = mini_movie_frame[item].apply(currency)

# output table with ticket data
print()
print(mini_movie_frame)

print()
print(f"you have sold all({tickets_sold}) tickets")
time.sleep(3)
