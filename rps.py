import random

def play_rps():
  """
  Plays a round of Rock-Paper-Scissors against the computer.
  """
  # Get user input
  user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

  # Validate user input
  valid_choices = ["rock", "paper", "scissors"]
  if user_choice not in valid_choices:
    print("Invalid choice. Please try again.")
    return

  # Generate computer's choice
  computer_choice = random.choice(valid_choices)

  # Determine winner
  win_conditions = {
    "rock": {"scissors": True},
    "paper": {"rock": True},
    "scissors": {"paper": True}
  }

  if user_choice == computer_choice:
    print("It's a tie!")
  elif win_conditions[user_choice].get(computer_choice):
    print("You win!")
  else:
    print("You lose. Computer chose", computer_choice)

if __name__ == "__main__":
  play_rps()
