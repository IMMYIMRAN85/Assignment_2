import random

def play_once():
    secret = random.randint(1, 10)
    guess = int(input("Guess a number 1-10: "))
    if guess == secret:
        print("Correct!")
    else:
        print(f"Nope, it was {secret}")

def main():
    print("=== Guess 1–10 (Replay Enabled) ===")
    while True:
        play_once()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()


