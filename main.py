from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player

def user_interaction():
    print("Welcome to the Rock-Paper-Scissors game!")

    # Dictionary to map player names to their respective functions
    player_functions = {
        'player': player,
        'mrugesh': mrugesh,
        'abbey': abbey,
        'quincy': quincy,
        'kris': kris,
        'human': human,
        'random_player': random_player
    }

    # Ask the user if they want to test players or play against one of the AI players
    action = input("Would you like to [1] test players or [2] play against one of them? Enter 1 or 2: ")

    if action == "1":
        # Test players against each other
        print("You can test the match by entering player names.")
        player1_name = input("Enter the name of the AI player (mrugesh, abbey, quincy, kris, random_player, player): ").lower()
        player2_name = input("Enter the name of the AI player (mrugesh, abbey, quincy, kris, random_player, player): ").lower()
        num_games = int(input("Enter the number of rounds to play: "))

        # Get the player functions from the dictionary
        player1 = player_functions.get(player1_name)
        player2 = player_functions.get(player2_name)

        play(player1, player2, num_games)


    elif action == "2":
        # User wants to play against one of the AI players
        print("You can play against one of the AI players.")
        player_name = input("Enter the name of the AI player (mrugesh, abbey, quincy, kris, random_player, player): ").lower()
        num_games = int(input("Enter the number of rounds to play: "))

        # Get the player function from the dictionary
        player1 = human  # The human player
        player2 = player_functions.get(player_name)

        play(player1, player2, num_games, verbose=True)


    else:
        print("Invalid choice. Please restart the program and choose 1 or 2.")

# Call the user interaction function to start the game
user_interaction()