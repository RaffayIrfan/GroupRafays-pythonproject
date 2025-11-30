import random
import time

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return f"Error: Invalid operation '{operation}'. Use '+', '-', '*', or '/'."

result_add = calculate(10, 5, '+')
print(f"10 + 5 = {result_add}")

result_sub = calculate(50.5, 12, '-')
print(f"50.5 - 12 = {result_sub}")

result_mul = calculate(7, 8.5, '*')
print(f"7 * 8.5 = {result_mul}")

result_div = calculate(100, 4, '/')
print(f"100 / 4 = {result_div}")

result_zero_div = calculate(9, 0, '/')
print(f"9 / 0 = {result_zero_div}")

result_invalid = calculate(15, 3, '%')
print(f"15 % 3 = {result_invalid}")

def guess_the_number():
    """
    Number Guessing Game, including the replay loop.
    """
    # Outer loop allows the user to play multiple rounds
    while True:
        LOWER_BOUND = 1
        UPPER_BOUND = 50
        secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)
        
        attempts = 0
        guess = None

        print("-" * 50)
        print(f"I'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}.")
        print("Can you guess what it is?")
        print("-" * 50)

        # Inner loop runs for one single game
        while guess != secret_number:
            try:
                guess_input = input("Enter your guess: ")
                guess = int(guess_input)
                
                attempts += 1
                
                if guess < LOWER_BOUND or guess > UPPER_BOUND:
                    print(f"Please guess a number strictly between {LOWER_BOUND} and {UPPER_BOUND}.")
                    attempts -= 1 
                elif guess < secret_number:
                    print("Too low! Try a higher number.")
                elif guess > secret_number:
                    print("Too high! Try a lower number.")
                
            except ValueError:
                print("Invalid input. Please enter a whole number.")
            except KeyboardInterrupt:
                print("\nGame interrupted. Goodbye!")
                return

        # Game end message
        print("\nCONGRATULATIONS!")
        print(f"You guessed the number {secret_number} correctly.")
        print(f"It took you {attempts} attempts to win.")
        
        # Ask for replay
        print("\n" + "=" * 50)
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        print("=" * 50)

        if play_again not in ('yes', 'y'):
            print("Thanks for playing! Goodbye!")
            break
        else:
            time.sleep(1)

guess_the_number()