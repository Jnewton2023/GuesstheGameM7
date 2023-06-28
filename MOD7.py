import random

def play_guessing_game():
    """
    This function allows the user to play a number guessing game.
    It generates a random number between 1 and 50 and prompts the user to guess the number.
    It provides feedback if the guess is too low or too high and keeps track of the number of attempts.
    It returns the total number of attempts.
    """
    classified_number = random.randint(1, 50)
    guess = 0
    attempts = 0

    while guess != classified_number:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1

        if guess < classified_number:
            print("Number is too low! Try again.")
        elif guess > classified_number:
            print("Number is too high! Try again.")

    print("Congratulations! You've found the secret number!")
    return attempts

def main():
    """
    This is the main function that calls the play_guessing_game() function to start the game.
    It stores the number of attempts in a list and displays the game result along with the attempts.
    """
    attempts_list = []
    num_games = 3

    for game in range(num_games):
        print(f"\nGame {game+1}:")
        attempts = play_guessing_game()
        attempts_list.append(attempts)

    print("\nGame Results:")
    for i, attempts in enumerate(attempts_list):
        print(f"Game {i+1}: Total attempts: {attempts}")

# Call the main function to start the game
main()
