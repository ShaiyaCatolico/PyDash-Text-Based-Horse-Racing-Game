import random

points = 100
provided_horses = [{"name": "Shadow", "color": "Gray 🔘"},{"name": "Rusty", "color": "Brown 🟤"}, 
                   {"name": "Daisy", "color": "White ⚪"},{"name": "Spirit", "color": "Gray 🔘"}, 
                   {"name": "Thunder", "color": "Black ⚫"},{"name": "Cinnamon", "color": "Brown 🟤"}, 
                   {"name": "Buster", "color": "White ⚪"}]

while True:
    print("\nWelcome to PyDash!")
    print("This is a game simulating a horse race using text only.")
    print(f"You currently have {points} points")
    print("\nChoose your horse:")
    print("1. Name and customize my horse")
    print("2. Use a random provided horse")

    while True:
        try:
            choice = int(input("\nEnter choice 1 or 2: "))
            if choice == 1:
                user_name = input("\nEnter your horse's name: ")
                print("\nChoose a color:")
                print("1. Brown 🟤")
                print("2. Black ⚫")
                print("3. White ⚪")
                print("4. Gray 🔘")
                color_choice = int(input("\nEnter a number 1–4: "))
                if color_choice == 1:
                    user_color = "Brown 🟤"
                elif color_choice == 2:
                    user_color = "Black ⚫"
                elif color_choice == 3:
                    user_color = "White ⚪"
                elif color_choice == 4:
                    user_color = "Gray 🔘"
                else:
                    print("Invalid color choice.")
                print(f"\nYour horse is: {user_name} ({user_color})")
            elif choice == 2: 
                chosen = random.choice(provided_horses) 
                user_name = chosen["name"] 
                user_color = chosen["color"] 
                print(f"\nYour horse is: {user_name} {user_color}")
            else:
                print("Invalid choice.")
                continue
            break
        except ValueError:
            print("Error. Please enter a number 1 or 2.")
        

    player_horse = user_name + " (" + user_color + ")"
    horses = [player_horse]
    for horse in provided_horses:
        full_name = horse["name"] + " (" + horse["color"] + ")"
        if full_name != player_horse:
            horses.append(full_name)

    while True:
        try:
            bet = int(input(f"\nHow many points do you want to bet? (Current points: {points}): "))
            if bet <= 0:
                print("Bet must be greater than zero.")
            elif bet > points:
                print("Not enough points.")
            else:
                break
        except ValueError:
            print("Error. Must be a number.")

    positions = []
    for i in range(len(horses)):
        positions.append(0)

    finish_line = 100
    winner = ""

    input("\nPress ENTER to start the race!")

    while winner == "":
        for i in range(len(horses)):
            positions[i] += random.randint(1, 5)
            if positions[i] >= finish_line and winner == "":
                winner = horses[i]

        for i in range(len(horses)):
            track_length = min(positions[i], finish_line)
            track = "-" * track_length + "🐎"
            print(f"{horses[i]}: {track}")
        
        if winner == "":
            input("\nPress Enter to continue...")

    print(f"\nThe winner is: {winner}")

    if winner == player_horse:
        print(f"You won! Current points: {points}")
        points += bet
    else:
        print(f"You lost. Current points: {points}")
        points -= bet

    if points <= 0:
        restart = input("\nYou ran out of points. Restart? (Y/N): ").upper()
        if restart == "Y":
            points = 100
            continue
        else:
            print("Thanks for playing!")
            break

    play_again = input("\nDo you want to play again? (Y/N): ").upper()
    if play_again != "Y":
        print("Game over.")
        break