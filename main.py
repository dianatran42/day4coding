import random

# random_integer = random.randint(1,10)
# print(random_integer)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random_float = random.uniform(0, 1)
# print(random_float)

# random_heads_or_tails = random.randint(0,1)
# if random_heads_or_tails == 0:
#     print("Heads")
# else:
#     print("Tails")

# list dau []

# luu ten cac quoc gia
# states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas",
#                      "California", "Colorado", "Connecticut",
#                      "Delaware", "Florida", "Georgia", "Hawaii",
#                      "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
#                      "Kentucky", "Louisiana", "Maine", "Maryland",
#                      "Massachusetts", "Michigan", "Minnesota",
#                      "Mississippi", "Missouri", "Montana", "Nebraska",
#                      "Nevada", "New Hampshire", "New Jersey", "New Mexico",
#                      "New York", "North Carolina", "North Dakota", "Ohio",
#                      "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
#                      "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
#                      "Vermont", "Virginia", "Washington", "West Virginia"]

# print(states_of_america[0])

# friends = ["Alice", "Bob", "Charlie", "David", "Diana"]
# # 1 option
# print(random.choice(friends))
# # 2nd option
# random_index = random.randint(0,4)
# print(friends[random_index])

# print(len(states_of_america))
# print(states_of_america[47])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
# vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])
# print(dirty_dozen[1][1])

import random

choices = ["Rock", "Paper", "Scissors"]

# User chooses
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

# Computer chooses randomly
computer_choice = random.randint(0, 2)

print("You choose:", choices[user_choice])
print("Computer chooses:", choices[computer_choice])

# Compare results
if user_choice == computer_choice:
    print("It's a draw 🤝")
elif (
    (user_choice == 0 and computer_choice == 2) or  # Rock beats Scissors
    (user_choice == 2 and computer_choice == 1) or  # Scissors beats Paper
    (user_choice == 1 and computer_choice == 0)     # Paper beats Rock
):
    print("You win 🎉")
else:
    print("You lose 😢")



