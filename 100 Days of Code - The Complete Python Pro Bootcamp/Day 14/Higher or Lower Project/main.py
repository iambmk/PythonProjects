# display art
from art import *
from game_data import *
import random

def format_data(account):
    """Takes account data and returns in the printable format"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Takes user guess and checks whether they have the correct answer"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    #Format th account data into printable format.
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)
    #check if user is correct
    # get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # use if statement to check if user is correct
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False


# score keeping


# make the game repeatable

# Making account at position B becomes the next account at position A.
