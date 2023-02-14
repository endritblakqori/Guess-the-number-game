import random
import time


# Exit function will ask user if they want to play again when user loses the game
def exit_game():
    while True:
        print("\n")
        y = input("If you want to play again press Y, if not press N: ").lower()
        print("\n")
        if y == "n":
            print("Thank you for playing!")
            exit()
        elif y == "y":
            game()
        else:
            print("Only press Y if you want to play again or N to exit!")


# Game function
def game():
    target_num = random.randint(1, 100)
    count = 1
    # while loop to ask the user for the number until they guess right or lose the game
    while count <= 7:
        try:
            guess_num = int(input("Write a number from 1 to 100:>> "))
            if guess_num < 1 or guess_num > 100:
                print("Please only write numbers from 1 to 100")
            elif guess_num > target_num:
                count += 1
                print("Your number", guess_num, "is bigger than the right number! Try a lower number!")
                print("You have", 8 - count, "tries left!")
            elif guess_num < target_num:
                count += 1
                print("Your number", guess_num, "is smaller than the right number! Try a higher number!")
                print("You have", 8 - count, "tries left!")
            elif guess_num == target_num:
                print("*Congratulations!* You have guessed the right number", target_num)
                print("\n")
                while True:
                    x = input(
                        "If you want to play again press Y, if not press N: ").lower()
                    if x == "n":
                        print("Thank you for playing!")
                        exit()
                    elif x == "y":
                        game()
                    else:
                        print("Only press Y if you want to play again or N to exit!")
        # Value error if user writes a letter or float number instead of int number
        except ValueError:
            print("Please only write numbers from 1 to 100")
    print(f"You have lost! You have no more tries left!")
    exit_game()


# simple function that displays a message when user starts playing
def play_game():
    print("***  Welcome to the 'Guess the number' game. To win, you need to guess the right number from 1 to 100  ***")
    print("                       ***  You have 7 tries to guess the number  ***                              ")
    print("\n")
    time.sleep(0.5)
    game()


play_game()
