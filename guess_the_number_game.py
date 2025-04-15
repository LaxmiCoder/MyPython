import random

def guess_the_number():
    print("Welcome to the 'Guess the Number' game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def select_difficulty():
    print("Select difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            return 50
        elif choice == '2':
            return 100
        elif choice == '3':
            return 200
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
