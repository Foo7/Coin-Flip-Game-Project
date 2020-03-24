import random
import time

def checkhistory(coin_wins, coin_losses, dice_wins, dice_losses):
    coin_total = coin_wins + coin_losses
    dice_total = dice_wins + dice_losses
    
    print("\nFetching wins/losses history")
    time.sleep(1.00)
    print("\n.🐌 ")
    time.sleep(0.50)
    print("\n...🐌 ")
    time.sleep(0.50)
    print("\n.....🐌 ")
    time.sleep(1.00)

    if coin_total == 0 and dice_total == 0:
        print("\nYou must play a game first!")
        time.sleep(1.50)
        return "\nReturning to main menu."
    
    #User Story: As a user I want to clearly see the updated guess history (correct count/total count).
    elif coin_total == 0:
        print("\nYou have played 0 times to Coins" + 
                "\nYou have played " + str(dice_total) + " times to Dice, winning {0} times and loosing {1} times for a ".format(dice_wins, dice_losses) + 
                str(round(dice_wins / dice_total * 100, 1)) + "% win ratio!")
        time.sleep(1.50)
        return "\nReturning to main menu."

    elif dice_total == 0:
        print("\nYou have played " + str(coin_total) + " times to Coins, winning {0} times and loosing {1} times for a ".format(coin_wins, coin_losses) + 
                str(round(coin_wins / coin_total * 100, 1)) + "% win ratio!" + 
                "\nYou have played 0 times to Dice")
        time.sleep(1.50)
        return "\nReturning to main menu."

    else:
        print("\nYou have played " + str(coin_wins + coin_losses) + " times to Coins, winning {0} times and loosing {1} times for a ".format(coin_wins, coin_losses) + 
                str(round(coin_wins / (coin_wins + coin_losses) * 100, 1)) + "% win ratio!" + 
                "\nYou have played " + str(dice_wins + dice_losses) + " times to Dice, winning {0} times and loosing {1} times for a ".format(dice_wins, dice_losses) + 
                str(round(dice_wins / (dice_wins + dice_losses) * 100, 1)) + "% win ratio!")
        time.sleep(1.50)
        return "\nReturning to main menu."

#----------------------------------------------------------------------------------------------------------------------------
# COIN FLIP

def coin_flip(coin_wins, coin_losses):
    flip_result = random.randint(1, 2)

    if flip_result == 1:
        flip_result = ["Heads", "heads"]
    else:
        flip_result = ["Tails", "tails"]
    
#User Story: As a user I want to be able to guess the outcome of a random coin flip(heads/tails).
    while True:
        time.sleep(0.5)
        player_call = input("\nAllright, let's play some Coin Flip!\nCall Heads or Tails and press enter to flip the coin: ")
        if player_call in ("Heads", "heads", "Tails", "tails"):
            break

    time.sleep(0.5)
    print("\nThe coin is in the air! 🤞")
    time.sleep(0.5)
    print("\n 🌕")
    time.sleep(0.5)
    print("\n      🌓")
    time.sleep(0.5)
    print("\n           🌕")
    time.sleep(0.5)
    print("\n                 🌗")
    time.sleep(1.0)

#User Story: As a user I want to clearly see the result of the coin flip.
#User Story: As a user I want to clearly see whether or not I guessed correctly.
    if player_call in flip_result:
        print("\nIt's " + player_call.title() + "! You win! 😎")
        coin_wins += 1
        coin_losses += 0
        time.sleep(2.0)
        return coin_wins, coin_losses

    elif flip_result != player_call:
        print("\nIt's " + str(flip_result[0]) + "! You Lose! 😓")
        coin_wins += 0
        coin_losses += 1
        time.sleep(2.0)
        return coin_wins, coin_losses


#----------------------------------------------------------------------------------------------------------------------------
# DICE

#User Story: As a user I want to be able to guess the outcome of a 6-sided dice roll (1-6), with the same feature set as the coin flip.
def dice(dice_wins, dice_losses):
    while True:
        time.sleep(0.5)
        player_call = input("\nAwesome! Let's roll the dice!\nCall a number between 1 and 6 and press enter to roll the dice: ").lower()
        if player_call in ("1", "2", "3", "4", "5", "6"):
            break

    if type(player_call) == str:
        
        dice = random.randint(1, 6)
        
        time.sleep(0.5)
        print("\nThe dice is rolling! 🍀")
        time.sleep(0.5)
        print("\n 🎲")
        time.sleep(0.5)
        print("\n     🎲")
        time.sleep(0.5)
        print("\n          🎲")
        time.sleep(0.5)
        print("\n               🎲")
        time.sleep(1.0)
       
        if str(dice) == player_call:
            print("\nIt's " + str(player_call) + "! You Win! 😎")
            dice_wins += 1
            dice_losses += 0
            time.sleep(2.0)
            return dice_wins, dice_losses

        elif str(dice) != player_call:
            print("\nIt's " + str(dice) + "! You Loose! 😓")
            dice_wins += 0
            dice_losses += 1
            time.sleep(2.0)
            return dice_wins, dice_losses



#----------------------------------------------------------------------------------------------------------------------------


def main():
    inputs_for_coinflip = {"c", "cf", "coin", "coinflip", "flip a coin", "flip", "1"}
    inputs_for_dice = {"d", "dice", "roll dice", "2"}
    coin_wins = 0
    coin_losses = 0
    dice_wins = 0
    dice_losses = 0
    while True:
        get_user_input = input("\n" +
                               "Please enter a game you would like to play - Coinflip or Dice \nAlternatively, type 'exit' to end the program or 'check' to see your wins/losses history: ").lower()

#User Story: As a user I want to be able to quit the game or go again after each cycle.
        if get_user_input == "exit" or get_user_input == "end":
            print("\n""See you again soon!")
            break

        elif get_user_input == "check":
            statement = checkhistory(coin_wins, coin_losses, dice_wins, dice_losses)
            print(statement)
            time.sleep(0.5)

        elif get_user_input in inputs_for_coinflip:
            coin_wins, coin_losses = coin_flip(coin_wins, coin_losses)

        elif get_user_input in inputs_for_dice:
            dice_wins, dice_losses = dice(dice_wins, dice_losses)

if __name__ == "__main__":
    main()





