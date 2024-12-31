import random
import options

options_list_icons = [options.rock, options.paper, options.scissors]
options_name = ["rock", "paper", "scissors"]
winning_options = [[0, 2], [1 , 0], [2, 1]]
valide_choices = [1, 2, 3]
user_score = 0
computer_score = 0

def who_wins_final():
  if computer_score == user_score:
1    print("We have a draw")
    return
  winner = "Computer wins!" if computer_score > user_score else "You win!"
  print(f"{winner}")
  exit(1)

def update_score(user_choice, computer_choice):
  global user_score, computer_score
  print([user_choice, computer_choice])
  if user_choice == computer_choice:
    user_score += 1
    computer_score += 1
    print("it's a draw")
  elif [user_choice, computer_choice] in winning_options:
    user_score += 1
    print("You won this round")
  else:
    computer_score += 1
    print("Computer won this round")


while True:
  try:
    choice = input("Choose rock(1), paper(2), scissors(3), stop the game(4):\n")


    if not int(choice) in valide_choices:
      print("this isn't a valide choice try again")
      continue
    elif choice == "4":
      print(f'''
      Thank for playing today, the final score is
      you: {user_score}
      computer: {computer_score}
      ''')
      who_wins_final()
    else:
      random_computer_choice = random.choice(valide_choices) - 1
      print(f'''
      you choose {options_name[int(choice) - 1]}:
      {options_list_icons[int(choice) - 1]}

      computer chooses {options_name[random_computer_choice]}:
      {options_list_icons[random_computer_choice]}
      ''')
      update_score(int(choice) - 1, random_computer_choice)
  except ValueError:
    print("Please enter a valid number.")