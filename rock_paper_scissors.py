import random

optionsInTheGame = ("rock", "paper", "scissors")

user = "nothing"
CPU = random.choice(optionsInTheGame)

while user not in optionsInTheGame:
    user = input("Please enter your option: ")

print(f"Your option: {user}")
print(f"CPU's option: {CPU}")

if user == CPU:
    print("That's a tie")
elif user == "rock" and CPU == "scissors":
    print("Hey, You won")
elif user == "paper" and CPU == "rock":
    print("Hey, You won")
elif user == "scissors" and CPU == "paper":
    print("Hey, You won")
else:
    print("Oops, You lost")




