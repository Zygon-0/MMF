import pandas
import random


# currency formatting function
def currency(num):
    return f"${num:.2f}"


# dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_tickets_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket price": all_tickets_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total cost (ticket = surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket price']
# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket price'] - 5

# chose raffle winner
winner_name = random.choice(all_names)

# get position of winner name in the list
win_index = all_names.index(winner_name)

# look up total amount won
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')
print(mini_movie_frame)

print()
print("---- Raffle Winner ----")
print(f"congratulations {winner_name}. you have won ${total_won:.2f} ie: your ticket is free!")

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# currency formatting
add_dollars = ['Ticket price', 'Surcharge', 'Total', 'Profit']
for item in add_dollars:
    mini_movie_frame[item] = mini_movie_frame[item].apply(currency)

# output table with ticket data
print(mini_movie_frame)

# output total ticket sales and profit
print(f"Total ticket sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")
