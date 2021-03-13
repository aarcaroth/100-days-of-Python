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
---'   ____)____
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

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
choice = int(choice) 

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")

roshambo = [rock, paper, scissors]

if choice == computer_choice:
  print(roshambo[choice])
  print(roshambo[computer_choice])
  print("There is a tie!")
elif choice >= 3 or choice < 0:
  print("You typed an invalid number, you lose!")
elif choice < computer_choice:
  print(roshambo[choice])
  print(roshambo[computer_choice])
  print("Computer Wins!")
elif (computer_choice == 0) and (choice == 2):
  print(roshambo[choice])
  print(roshambo[computer_choice])
  print("Computer Wins!")
elif (computer_choice == 2) and (choice == 0):
  print(roshambo[choice])
  print(roshambo[computer_choice])
  print("You Win!")
elif choice > computer_choice:
  print(roshambo[choice])
  print(roshambo[computer_choice])
  print("You Win!")
