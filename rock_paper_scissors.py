import random
#random module enables the AI to select any of the options randomly




possible_actions = ["rock", "paper", "scissors"]
#possible action is what the AI will choose from


#random.choice means AI should pick from the options provided in the possible actions


user_score = 0
AI_score = 0

def play():
    global user_score
    global AI_score
    global play
    while (True):
        if user_score == 2 or AI_score == 2:
            break
        else:
            user_action = input("Enter a choice (rock, paper, scissors): ")
            # user action takes input from the user
            computer_action = random.choice(possible_actions)
            if user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie!")
            elif user_action == "rock":
                if computer_action == "scissors":
                    print("Rock smashes scissors! You win!")
                    user_score += 1
                else:
                    print("Paper covers rock! You lose.")
                    AI_score += 1
            elif user_action == "paper":
                if computer_action == "rock":
                    print("Paper covers rock! You win!")
                    user_score += 1
                else:
                    print("Scissors cuts paper! You lose.")
                    AI_score += 1
            elif user_action == "scissors":
                if computer_action == "paper":
                    print("Scissors cuts paper! You win!")
                    user_score += 1
                else:
                    print("Rock smashes scissors! You lose.")
                    AI_score += 1
play()
retry = input("Press Y to restart or N to exit")
if retry == "Y" or "y":
    user_score = 0
    AI_score = 0    
    play()
