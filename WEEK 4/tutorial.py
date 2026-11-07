money_withdrawn=2350
notes=500
coins=50


num_of_five_hundred_naira_notes= money_withdrawn//notes



num_of_fifty_naira_coins= money_withdrawn%notes//coins



print(f"Number of 500 naira notes given is {num_of_five_hundred_naira_notes}")
print(f"Number of 50 naira coins given is {num_of_fifty_naira_coins}")
