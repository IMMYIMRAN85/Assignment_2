import random

def main():
    secret = random.randint(1, 10)
    guess = int(input("Guess a number 1-10: "))
    if guess == secret:
        print("Correct!")
    else:
        print(f"Nope, it was {secret}")
if __name__ == "__main__":
    main()
