import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("Choose your weapon! Type 0 for Rock 🪨, 1 for Paper 📄, or 2 for Scissors ✂️:\n"))

# Check if the user input is valid before accessing the list
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number. Please choose 0, 1, or 2 next time. You lose!") 
else:
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("Rock crushes Scissors. You win! 🎉")
    elif computer_choice == 0 and user_choice == 2:
        print("Rock crushes Scissors. You lose. 😢")
    elif computer_choice > user_choice:
        print(f"{game_images[computer_choice]} beats {game_images[user_choice]}. You lose. 😢")
    elif user_choice > computer_choice:
        print(f"{game_images[user_choice]} beats {game_images[computer_choice]}. You win! 🎉")
    elif computer_choice == user_choice:
        print("It's a draw. 🤝")
