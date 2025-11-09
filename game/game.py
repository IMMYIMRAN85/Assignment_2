
# overwrite with the tiny improved version (still only on this branch)

import random

def get_int(prompt):
    """Keep asking until user enters a valid number."""
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            return int(user_input)
        print(" Invalid input. Please enter a whole number 1–10.")

def main():
    print("=== Guess 1-10 ===")
    secret = random.randint(1, 10)
    guess = get_int("Your guess: ")

    if guess == secret:
        print(" Correct!")
    else:
        print(f" Nope, it was {secret}")

if __name__ == "__main__":
    main()


