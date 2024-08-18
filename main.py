import random

def display_menu():
    print("Welcome to the Number Guessing Game!")
    print("1. Play Game")
    print("2. Exit")

def play_game():
    min_number = 1
    max_number = 100
    number = random.randint(min_number, max_number)
    attempts = 0
    print(f"Guess a number between {min_number} and {max_number}. You have 6 attempts.")

    while attempts < 6:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == number:
                print(f"Congratulations! You guessed the number.")
                break
            elif guess < number:
                print("Try guessing higher.")
            else:
                print("Try guessing lower.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '_main_':
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        play_game()
    elif choice == '2':
        print("Exiting the game.")
    else:
        print("Invalid choice. Please try again.")