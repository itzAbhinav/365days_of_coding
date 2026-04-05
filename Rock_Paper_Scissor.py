import random as rand 

print("Welcome to Rock Paper Scissor game!!")
print()
user_points = 0
computer_points = 0
while True:
    print("Choose options: ")
    print("1. Rock , 2. Paper 3. Scissor 4. Quit")
    if user_points < 0 :
        user_points = 0 
    if computer_points < 0:
        computer_points = 0
    print(f"User_points: {user_points}  Computer_points: {computer_points}")
    print()
    option = ["rock","paper","scissor"]
    user_input = input("Enter the user input: ")
    computer_input = option[rand.randint(0,2)]
    print(f"Computer chose {computer_input.upper()}")
    if user_input.lower() == computer_input:
        print("Tie")
        print()
    elif (user_input.lower() == "rock" and computer_input == "paper") or (user_input.lower() == "paper" and computer_input == "scissor") or (user_input.lower() == "scissor" and computer_input == "rock"):
        computer_points += 1
        user_points -= 1
        print("Lost")
        print()
    elif (user_input.lower() == "rock" and computer_input == "scissor") or (user_input.lower() == "paper" and computer_input == "rock") or (user_input.lower() == "scissor" and computer_input == "paper"):
        computer_points -= 1
        user_points += 1
        print("Won")
        print()
    elif user_input.lower() == "quit" or user_input.lower() == "q":
        print("----- FINAL SCORE -------")
        print(f"User_points: {user_points}  Computer_points: {computer_points}")
        break    
    