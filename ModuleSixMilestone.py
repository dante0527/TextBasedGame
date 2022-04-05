# Dante Lee


# Gameplay loop
if __name__ == '__main__':
    # A dictionary for the simplified dragon text game
    # The dictionary links a room to other rooms
    rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
        }

    # Variable to track current room
    # Initialized with starting room
    current_room = "Great Hall"
    # Tracks the environment of current_room
    environment = rooms[current_room]

    while True:
        # Start-of-turn message
        print(f"\nYou are in the {current_room}\n{'-' * 27}")

        # Accepts user input
        user_input = input('Enter your move:\n')
        # Splits move into words
        next_move = user_input.split(' ')
        # action determines what the user wants to do
        # direction determines where the action is directed
        action = next_move[0]
        if len(next_move) > 1:
            direction = next_move[1].title()

        # If the action is 'go',
        #   set current_room to the room associated with direction
        if action == 'go':
            try:
                current_room = rooms[current_room][direction]
            except:
                print("You can't go that way.")
                pass
        # Exit command breaks while-loop and terminates program
        elif action == 'exit':
            break
        # If user_input is invalid, the user is notified and the while-loop continues
        else:
            print("Invalid command")
