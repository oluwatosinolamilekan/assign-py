import random

def hi_low_game():
    secret_number = random.randint(0, 100)
    
    while True:
        user_guess = int(input("Guess the number (between 0 and 100): "))
        
        if user_guess < 0 or user_guess > 100:
            print("Quitting the game.")
            break
        
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number}.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    hi_low_game()
