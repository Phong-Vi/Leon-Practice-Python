import random

def guess_my_number(name):
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to 'Guess My Number'!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Higher...")
        elif guess > number_to_guess:
            print("Lower...")
        else:
            print(f"Congratulations 🎉 {name}! You guessed the number in {attempts} attempts.")
            answer = input(f"\nPlay again, {name} [y|n]?\n").lower()
            if answer == "y" or answer == "yes":
                guess_my_number(name)
            else:
                print(f"Goodbye {name}. Have a nice day 👋!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personalized game of 'Guess My Number'."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=False,
        default="Anonymous",
        help="The name of the person playing the 'Guess My Number'."
    )
    args = parser.parse_args()

    guess_my_number(args.name)