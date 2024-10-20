from random import randint, choice, shuffle, random


def reset_matrix():
    for key, value in game_matrix_dict.items():
        game_matrix_dict[key][1] = False
        game_matrix_dict[key][2] = ""
        print_matrix()


def print_matrix():
    # set up a print layout that is easy to read
    print()
    print("*" * 50)
    print("Game Matrix")
    counter = 1
    rows = []
    columns = []
    for key, value in game_matrix_dict.items():
        if value[1]:
            square_value = value[2]
        else:
            square_value = "-"
        columns.append(square_value)
        if counter == 3 or counter == 6 or counter == 9:
            rows.append(columns)
            columns = []
        counter += 1
    for row in rows:
        print(row[0], row[1], row[2])
    print("*" * 50)
    print()


def set_selection(i, j, player):
    print(
        f"==================    Selection Made: sq: ({i}, {j}) -- player: {player} =================="
    )
    # loop through the game_matrix_dict and set the player
    for key, value in game_matrix_dict.items():
        if value[0] == (i, j):
            game_matrix_dict[key][1] = True
            game_matrix_dict[key][2] = player

    print_matrix()


def get_empty_squares() -> list:  # returns a list of empty squares
    empty_squares = []
    for key, value in game_matrix_dict.items():
        if not value[1]:
            empty_squares.append(value[0])
    print(f"Empty Squares: {empty_squares}")
    print()
    return empty_squares


def easy_move(player: str):
    print("--- Making an easy move ---")
    print(f"Player: {player}")
    print()
    # make a random selection from any of the empty squares
    empty_squares = get_empty_squares()
    computer_choice = choice(empty_squares)
    # return the computer choice of the game_matrix_dict
    for key, value in game_matrix_dict.items():
        if value[0] == computer_choice:
            # set the computer choice to "O"
            set_selection(computer_choice[0], computer_choice[1], player)
            # game_matrix_dict[key][1] = True
            # game_matrix_dict[key][2] = player
            # print_matrix()
    print(f"Game Matrix: {game_matrix_dict}")
    return


def medium_move(player: str):
    print("--- Making an medium move ---")
    print(f"Player: {player}")
    print()
    # Implement a basic strategy here
    # take the game board and:
    # 1. checks for a winning move for the computer player
    # it looks for a row, column or diagonal where the computer player has 2 out of 3 squares, and the third square is empty
    # then it returns that empty square to win the game

    # 2. if no winning move is found, then it gets the empty squares that are adjacent to the player's squares, if an empty square is next to a players square, then it puts that square in the list of possible moves (this is medium difficulty, that's why it doesn't check for the player's winning moves)
    # 3. return a random square from the list of possible moves
    empty_squares = get_empty_squares()
    # check for a winning move for the computer player
    # check if player is on the board at all first
    if len(empty_squares) == 9:
        computer_choice = choice(empty_squares)
        # return the computer choice of the game_matrix_dict
        for key, value in game_matrix_dict.items():
            if value[0] == computer_choice:
                # set the computer choice to "O"
                game_matrix_dict[key][1] = True
                game_matrix_dict[key][2] = player
                print_matrix()
        print(f"Game Matrix: {game_matrix_dict}")
        return

    # get a list of squares that are adjacent to the human player (not the computer player)
    # print()
    # print(f"__ before: Game Matrix: {game_matrix_dict}")
    # print()
    opponent_squares = []
    computer_squares = []
    available_squares = []

    for key, value in game_matrix_dict.items():
        if game_matrix_dict[key][2] != player and game_matrix_dict[key][1] == True:
            opponent_squares.append(game_matrix_dict[key][0])
        if game_matrix_dict[key][2] == player:
            computer_squares.append(game_matrix_dict[key][0])
        # if game_matrix_dict[key][1] == False:
        #     available_squares.append(game_matrix_dict[key][0])

    print(f"Opponent Squares: {opponent_squares}")
    print(f"Computer Squares: {computer_squares}")
    # print(f"Available Squares: {available_squares}")
    print()

    adjacent_squares = []
    # get a list of squares that are adjacent to the opponent_squares
    for square in opponent_squares:
        # print(f"SQUARE: {square}")
        # print("-" * 25)
        # print(f"Top Left: ({square[0]-1}, {square[1]-1})")
        # print(f"Top: ({square[0] - 1}, {square[1]})")
        # print(f"Top Right: ({square[0]-1}, {square[1]+1})")
        # print(f"Left: ({square[0]}, {square[1]-1})")
        # print(f"Right: ({square[0]}, {square[1]+1})")
        # print(f"Bottom Left: ({square[0]+1}, {square[1]-1})")
        # print(f"Bottom: ({square[0] + 1}, {square[1]})")
        # print(f"Bottom Right: ({square[0]+1}, {square[1]+1})")
        # print()

        for key, value in game_matrix_dict.items():
            # Check each square around the opponent square (row, col) - (0,0)

            #             -1,-1    -1,0    -1,+1
            #              0,-1    0,0    0,+1
            #             +1,-1    +1,0    +1,+1

            if (
                game_matrix_dict[key][0] == (square[0] - 1, square[1])  # top
                or game_matrix_dict[key][0] == (square[0] + 1, square[1])  # bottom
                or game_matrix_dict[key][0] == (square[0], square[1] - 1)  # left
                or game_matrix_dict[key][0] == (square[0], square[1] + 1)  # right
                or game_matrix_dict[key][0]
                == (square[0] - 1, square[1] - 1)  # top left
                or game_matrix_dict[key][0]
                == (square[0] + 1, square[1] + 1)  # bottom right
                or game_matrix_dict[key][0]
                == (square[0] - 1, square[1] + 1)  # top right
                or game_matrix_dict[key][0]
                == (square[0] + 1, square[1] - 1)  # bottom left
            ):
                # check that the square is not a computer square or an opponent square and not already in the adjacent_squares list
                if (
                    game_matrix_dict[key][0] not in computer_squares
                    and game_matrix_dict[key][0] not in opponent_squares
                    and game_matrix_dict[key][0] not in adjacent_squares
                ):
                    adjacent_squares.append(game_matrix_dict[key][0])


def hard_move(player: str):
    print("--- Making an hard move ---")
    print(f"Player: {player}")
    print()

    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    # Implement a basic strategy here
    # take the game board and:
    # 1. checks for a winning move for the computer player first
    # it looks for a row, column or diagonal where the computer player has 2 out of 3 squares, and the third square is empty
    # then it returns that empty square to win the game or block the other player from winning
    # 2. if no winning move is found, then it gets the empty squares that are adjacent to the player's squares, if an empty square is next to a players square, then it puts that square in the list of possible moves (this is medium difficulty, that's why it doesn't check for the player's winning moves)

    empty_squares = get_empty_squares()
    # check for a winning move for the computer player
    # check if player is on the board at all first
    print(f"Length of empty_squares: {len(empty_squares)}")
    if len(empty_squares) == 9:
        computer_choice = choice(empty_squares)
        set_selection(computer_choice[0], computer_choice[1], player)
        # return the computer choice of the game_matrix_dict
        # for key, value in game_matrix_dict.items():
        #     if value[0] == computer_choice:
        #         # set the computer choice to "O"
        #         game_matrix_dict[key][1] = True
        #         game_matrix_dict[key][2] = player
        #         print_matrix()
        print(f"Game Matrix: {game_matrix_dict}")
        return

    # get a list of squares that are adjacent to the human player (not the computer player)
    # print()
    # print(f"__ before: Game Matrix: {game_matrix_dict}")
    # print()
    opponent_squares = []
    player_squares = []
    block_or_win_squares = []

    for key, value in game_matrix_dict.items():
        if game_matrix_dict[key][2] != player and game_matrix_dict[key][1] == True:
            opponent_squares.append(game_matrix_dict[key][0])
        if game_matrix_dict[key][2] == player:
            player_squares.append(game_matrix_dict[key][0])

    print(f"Opponent Squares: {opponent_squares}")
    print(f"Player Squares: {player_squares}")
    # print(f"Available Squares: {available_squares}")
    print()

    # check if the player has two squares adjacent to each other either horizontally, vertically or diagonally
    print(f"Length of player_squares: {len(player_squares)}")
    if len(player_squares) >= 2:
        has_two = check_for_two(player)
        print(f"Has Two - Open Square: {has_two}")
        if has_two:
            # set the square selection to the has_two
            set_selection(has_two[0][0], has_two[0][1], player)
            print(f"Game Matrix: {game_matrix_dict}")
            return
    # check if the opponent has two squares adjacent to each other either horizontally, vertically or diagonally
    print(f"Length of opponent_squares: {len(opponent_squares)}")
    if len(opponent_squares) >= 2:
        has_two = check_for_two(opponent)
        print(f"Has Two - Open Square: {has_two}")
        if has_two:
            # set the square selection to the has_two
            set_selection(has_two[0][0], has_two[0][1], player)
            print(f"Game Matrix: {game_matrix_dict}")
            return

    adjacent_squares = []
    # get a list of squares that are adjacent to the opponent_squares
    for square in opponent_squares:
        # print(f"SQUARE: {square}")
        # print("-" * 25)
        # print(f"Top Left: ({square[0]-1}, {square[1]-1})")
        # print(f"Top: ({square[0] - 1}, {square[1]})")
        # print(f"Top Right: ({square[0]-1}, {square[1]+1})")
        # print(f"Left: ({square[0]}, {square[1]-1})")
        # print(f"Right: ({square[0]}, {square[1]+1})")
        # print(f"Bottom Left: ({square[0]+1}, {square[1]-1})")
        # print(f"Bottom: ({square[0] + 1}, {square[1]})")
        # print(f"Bottom Right: ({square[0]+1}, {square[1]+1})")
        # print()

        for key, value in game_matrix_dict.items():
            # Check each square around the opponent square (row, col) - (0,0)

            #             -1,-1    -1,0    -1,+1
            #              0,-1    0,0    0,+1
            #             +1,-1    +1,0    +1,+1

            if (
                game_matrix_dict[key][0] == (square[0] - 1, square[1])  # top
                or game_matrix_dict[key][0] == (square[0] + 1, square[1])  # bottom
                or game_matrix_dict[key][0] == (square[0], square[1] - 1)  # left
                or game_matrix_dict[key][0] == (square[0], square[1] + 1)  # right
                or game_matrix_dict[key][0]
                == (square[0] - 1, square[1] - 1)  # top left
                or game_matrix_dict[key][0]
                == (square[0] + 1, square[1] + 1)  # bottom right
                or game_matrix_dict[key][0]
                == (square[0] - 1, square[1] + 1)  # top right
                or game_matrix_dict[key][0]
                == (square[0] + 1, square[1] - 1)  # bottom left
            ):
                # check that the square is not a computer square or an opponent square and not already in the adjacent_squares list
                if (
                    game_matrix_dict[key][0] not in player_squares
                    and game_matrix_dict[key][0] not in opponent_squares
                    and game_matrix_dict[key][0] not in adjacent_squares
                ):
                    adjacent_squares.append(game_matrix_dict[key][0])

    print()
    print(f"Adjacent Squares: {adjacent_squares}")
    print()

    # Now make a choice of the adjacent squares
    adj_choice = choice(adjacent_squares)
    print(f"Adjacent Squares Choice: {adj_choice}")
    print()

    # set the square selection to the adj_choice
    set_selection(adj_choice[0], adj_choice[1], player)

    print(f"Game Matrix: {game_matrix_dict}")
    return


def check_for_two(player: str):
    # check for 2 squares in a row, column or diagonal for the player
    # returns the third square if found and None if not found
    for key, value in game_matrix_dict.items():
        # check the rows
        if (
            game_matrix_dict["sq1"][2] == player
            and game_matrix_dict["sq2"][2] == player
            and game_matrix_dict["sq3"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq3"]
        elif (
            game_matrix_dict["sq1"][2] == player
            and game_matrix_dict["sq3"][2] == player
            and game_matrix_dict["sq2"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq2"]
        elif (
            game_matrix_dict["sq2"][2] == player
            and game_matrix_dict["sq3"][2] == player
            and game_matrix_dict["sq1"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq1"]
        elif (
            game_matrix_dict["sq4"][2] == player
            and game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq6"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq6"]
        elif (
            game_matrix_dict["sq4"][2] == player
            and game_matrix_dict["sq6"][2] == player
            and game_matrix_dict["sq5"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq5"]
        elif (
            game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq6"][2] == player
            and game_matrix_dict["sq4"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq4"]
        elif (
            game_matrix_dict["sq7"][2] == player
            and game_matrix_dict["sq8"][2] == player
            and game_matrix_dict["sq9"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq9"]
        elif (
            game_matrix_dict["sq7"][2] == player
            and game_matrix_dict["sq9"][2] == player
            and game_matrix_dict["sq8"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq8"]
        elif (
            game_matrix_dict["sq8"][2] == player
            and game_matrix_dict["sq9"][2] == player
            and game_matrix_dict["sq7"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq7"]
        # check the columns
        elif (
            game_matrix_dict["sq1"][2] == player
            and game_matrix_dict["sq4"][2] == player
            and game_matrix_dict["sq7"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq7"]
        elif (
            game_matrix_dict["sq1"][2] == player
            and game_matrix_dict["sq7"][2] == player
            and game_matrix_dict["sq4"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq4"]
        elif (
            game_matrix_dict["sq4"][2] == player
            and game_matrix_dict["sq7"][2] == player
            and game_matrix_dict["sq1"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq1"]
        elif (
            game_matrix_dict["sq2"][2] == player
            and game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq8"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq8"]
        elif (
            game_matrix_dict["sq2"][2] == player
            and game_matrix_dict["sq8"][2] == player
            and game_matrix_dict["sq5"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq5"]
        elif (
            game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq8"][2] == player
            and game_matrix_dict["sq2"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq2"]
        elif (
            game_matrix_dict["sq3"][2] == player
            and game_matrix_dict["sq6"][2] == player
            and game_matrix_dict["sq9"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq9"]
        elif (
            game_matrix_dict["sq3"][2] == player
            and game_matrix_dict["sq9"][2] == player
            and game_matrix_dict["sq6"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq6"]
        elif (
            game_matrix_dict["sq6"][2] == player
            and game_matrix_dict["sq9"][2] == player
            and game_matrix_dict["sq3"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq3"]
        # check diagonals
        elif (
            game_matrix_dict["sq1"][2] == player
            and game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq9"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq9"]
        elif (
            game_matrix_dict["sq1"][2] == player
            and game_matrix_dict["sq9"][2] == player
            and game_matrix_dict["sq5"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq5"]
        elif (
            game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq9"][2] == player
            and game_matrix_dict["sq1"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq1"]
        elif (
            game_matrix_dict["sq3"][2] == player
            and game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq7"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq7"]
        elif (
            game_matrix_dict["sq3"][2] == player
            and game_matrix_dict["sq7"][2] == player
            and game_matrix_dict["sq5"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq5"]
        elif (
            game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq7"][2] == player
            and game_matrix_dict["sq3"][1] == False
        ):
            print(f"Player {player} has two squares!")
            print()
            return game_matrix_dict["sq3"]
        else:
            print("--- No two squares found! ---")
            print()
            return None


def check_for_winner(player: str):
    # check for a winner
    # check the rows
    # check the columns
    # check the diagonals
    # if there is a winner, then return the winner
    # if there is no winner, then return None

    # check for 3 in a row or column or diagonal for the player
    for key, value in game_matrix_dict.items():
        # check the rows
        if (
            game_matrix_dict["sq1"][2] == player
            and game_matrix_dict["sq2"][2] == player
            and game_matrix_dict["sq3"][2] == player
        ):
            print(f"Player {player} wins!")
            return True
        elif (
            game_matrix_dict["sq4"][2] == player
            and game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq6"][2] == player
        ):
            print(f"Player {player} wins!")
            return True
        elif (
            game_matrix_dict["sq7"][2] == player
            and game_matrix_dict["sq8"][2] == player
            and game_matrix_dict["sq9"][2] == player
        ):
            print(f"Player {player} wins!")
            return True
        # check the columns
        elif (
            game_matrix_dict["sq1"][2] == player
            and game_matrix_dict["sq4"][2] == player
            and game_matrix_dict["sq7"][2] == player
        ):
            print(f"Player {player} wins!")
            return True
        elif (
            game_matrix_dict["sq2"][2] == player
            and game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq8"][2] == player
        ):
            print(f"Player {player} wins!")
            return True
        elif (
            game_matrix_dict["sq3"][2] == player
            and game_matrix_dict["sq6"][2] == player
            and game_matrix_dict["sq9"][2] == player
        ):
            print(f"Player {player} wins!")
            return True
        # check the diagonals
        elif (
            game_matrix_dict["sq1"][2] == player
            and game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq9"][2] == player
        ):
            print(f"Player {player} wins!")
            return True
        elif (
            game_matrix_dict["sq3"][2] == player
            and game_matrix_dict["sq5"][2] == player
            and game_matrix_dict["sq7"][2] == player
        ):
            print(f"Player {player} wins!")
            return player
        else:
            print("--- No winner yet! ---")
            print()
            return False


def game_over_draw():
    print("&" * 50)
    print("        Game Over! It's a draw!")
    print("&" * 50)
    print()
    exit()


def game_over_winner(player):
    print("&" * 50)
    print("       Winner, Winner, Chicken Dinner!")
    print(f"     Game Over! - {player} is the winner!")
    print("&" * 50)
    print()
    exit()


game_matrix_dict = {
    "sq1": [(0, 0), False, ""],  # [position, is_clicked, player]
    "sq2": [(0, 1), False, ""],
    "sq3": [(0, 2), False, ""],
    "sq4": [(1, 0), False, ""],
    "sq5": [(1, 1), False, ""],
    "sq6": [(1, 2), False, ""],
    "sq7": [(2, 0), False, ""],
    "sq8": [(2, 1), False, ""],
    "sq9": [(2, 2), False, ""],
}


print()
print("o" * 50)
print("Tic-Tac-Toe Game")
print("o" * 50)
print()

print()
print("=== Setting up the game matrix ===")
for key, item in game_matrix_dict.items():
    print(key, item)

print("=================================")
print()

click_count = 0
print_matrix()
print()
# medium_move("X")
# print()
# medium_move("O")
# print()
# easy_move("X")
# print()
# medium_move("O")
# print()
# input("Press any key to continue...")
# print()

while click_count < 9:
    hard_move("X")
    click_count += 1
    print()
    if check_for_winner("X"):
        game_over_winner("X")
    if click_count == 9:
        game_over_draw()
    input("Press any key to continue...")
    print()
    hard_move("O")
    click_count += 1
    print()
    if check_for_winner("O"):
        game_over_winner("O")
    if click_count == 9:
        game_over_draw()
    input("Press any key to continue...")
    print()
game_over_draw()
