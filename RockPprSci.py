import random

choices = ["rock", "sci", "ppr"]

computer_choice = random.randint(0, 2)
computer_real_choice = choices[computer_choice]

user_choice = input("Choose: 0: rock, 1: scissors, 2: paper")
user_real_choice = choices[int(user_choice)]

results_table = {
    "rock": {
      "rock": 0,
      "sci": 1,
      "ppr": -1
    },
    "sci": {
      "rock": -1,
      "sci": 0,
      "ppr": 1
    },
    "ppr": {
      "rock": 1,
      "sci": -1,
      "ppr": 0
    },
}

game_result = results_table[computer_real_choice][user_real_choice]
print("Computer chose: " + computer_real_choice)
print("User chose: " + user_real_choice)

if(game_result == 0):
    print("Tie!")
elif(game_result == 1):
    print("Computer Won!")
else:
    print("User Won!")

