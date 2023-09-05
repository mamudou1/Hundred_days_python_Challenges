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

#Write your code below this line 👇
import random
game= [rock, paper, scissors]
user_choice = int(input("what do you want to choose: 0 for rock, 1 for paper, and 2 for scissors: "))
print(game[user_choice])

com_choice = random.randint(0,2)
print(game[com_choice])

if user_choice >= 3 or user_choice < 0:
    print("you enter and ivalid choice")
elif user_choice == 0 and com_choice == 2:
    print("you win")
elif com_choice ==0 and user_choice ==2:
    print("computer wins ")
elif user_choice > com_choice:
    print("you win")
elif com_choice > user_choice:
    print("Computer Wins!")
elif com_choice == user_choice:
    print("tie game!!")


