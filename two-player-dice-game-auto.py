"""
Created on Sun Jan 24 18:36:46 2021
@author: Chamath Wijaaysundara
"""
# Define the Lists to hold the user scores
import random as r

first_user_score = 0
second_user_score = 0
file_name = "dice-game-winners.txt"

# Dictionary      KEY          VALUE
loginDetails = {"user1" : "waterbottle12", "user2" : "iphone22"}

print(loginDetails)

def authenticate_player():
    while True:
        loginUsername = input("Enter Username : ")
        loginPassword = input("Enter Password : ")
        if loginUsername in loginDetails:
            if loginPassword == loginDetails[loginUsername]:
                player1_name = loginUsername
                print(player1_name, "Has Signed In!")
                return player1_name
                break
            else:
                print("Password is incorrect!")
        else:
            print("User does not exist")

def rollDice(player_name, round):
    print(player_name, end="")
    input(" press enter to roll")
    roll1 = r.randint(1, 6)
    roll2 = r.randint(1, 6)
    total = roll1 + roll2
    if total%2 == 0: # Even
        total += 10
    else:            # Odd
        total -= 5
    if roll1 == roll2:
        roll3 = r.randint(1, 6)
        total += roll3
        print('Total for ' + player_name + ' after the ' + str(round) + ' dice roll is : ' + str(total))
    return total

def roll_dice_game(player_name):
    i=1
    total_score = 0
    while i<6:
        total_score += rollDice(player_name, i)
        print(player_name + ' score after ' + str(i) + ' round is ' + str(total_score))
        i+=1
    return total_score

# Define a function to write to a file
def write_to_file(data):
    with open(file_name, 'a') as output:
        output.write(data + "\n")

def read_file():
    f = open(file_name, "r")
    print(f.read())
    f.close()

# Define a function to determine the winner
def determine_winner(player1, player_1_total_score, player2, player_2_total_score, round=6):
    if (player_1_total_score > player_2_total_score):
        print(player1, "Won the Game !!")
        winner_details = player1 + ":" + str(player_1_total_score)
        write_to_file(winner_details)
    elif (player_1_total_score < player_2_total_score):
        print(player2, "Won the Game !!")
        winner_details = player2 + ":" + str(player_2_total_score)
        write_to_file(winner_details)
    else:
        print('Rolling the dice agan to brek the tie !')
        score_1_equl = rollDice(player1,round)
        score_2_equl = rollDice(player2,round)
        player_1_total_score += score_1_equl
        player_2_total_score += score_2_equl
        # use recursion to break the tie !
        round += 1
        determine_winner(player1, player_1_total_score, player2, player_2_total_score, round)

print("Welcome to Dice Roll Game!")

player_1 = authenticate_player()
player_2 = authenticate_player()

first_user_score = roll_dice_game(player_1)
print(player_1 + ' total score is :', first_user_score)

second_user_score = roll_dice_game(player_2)
print(player_2 + ' total score is :', second_user_score)

determine_winner(player_1, first_user_score, player_2, second_user_score)

read_file()
