#choosing a random number between 1 and 100
import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check users guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the correct answer"""
    if user_guess > actual_answer:
          print("You guessed too high")
          return turns - 1
    elif user_guess < actual_answer:
          print("You guessed too low")
          return turns - 1
    else:
          print(f"You guessed correctly! The answer was {actual_answer}")
#function to set difficulty
def set_difficulty():
      level = input("choose a difficulty. Type 'easy' or 'hard':").lower()
      if level == "easy":
            return EASY_LEVEL_TURNS
      else:
            return HARD_LEVEL_TURNS
def play_game():
      print(art.logo)
      print("Welcome to the number guessing Game!"
            "I'm thinking of a number between 1 and 100")
      computer = random.choice(range(1 , 101))
      #Let the user guess a number
      turns = set_difficulty()
      guess = 0
      while guess != computer:
            print(f"You have {turns} attempts to guess the number.")
            guess = int(input("Make a guess: "))
            turns = check_answer(guess, computer, turns)
            if turns == 0:
                  print("you've run out of guesses, You lose!")
                  return
            elif guess != computer:
                  print("guess again")
play_game()





#Track the number of turns and reduce by 1 if they get it wrong

# Repeat the guessing functionality if they get it wrong.