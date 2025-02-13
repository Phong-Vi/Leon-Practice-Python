import guess_number
import rps_game

def main_menu(name):
    while True:
        print("Choose a game to play:")
        print("1. Guess the Number")
        print("2. Rock, Paper, Scissors")
        print("3. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            guess_number.guess_my_number(name)
        elif choice == '2':
            rps_game.play_game(name)
        elif choice == '3':
            print(f"Goodbye, {name}!")
            break
        else:
            print(f"Invalid choice, {name}. Please try again.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personalized arcade of games."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=False,
        default="Anonymous",
        help="The name of the person playing games."
    )
    args = parser.parse_args()

    main_menu(args.name)