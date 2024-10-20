from random import randint, choice, shuffle, random


class ComputerPlayer:
    def __init__(self, difficulty="easy", player="", gameboard=None):
        self.difficulty = difficulty
        self.player = player
        self.gameboard = gameboard

    def select_square(self, game_board):
        if self.difficulty == "easy":
            return self.easy_move(game_board)
        elif self.difficulty == "medium":
            return self.medium_move(game_board)
        elif self.difficulty == "hard":
            return self.hard_move(game_board)

    def easy_move(self, game_board):
        print("--- Making an easy move ---")
        print(f"Player: {self.player}")
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

        # make a random selection from any of the empty squares
        empty_squares = game_board.get_empty_squares()

        return choice(empty_squares)

    def medium_move(self, game_board):
        # Implement a basic strategy here
        # take the game board and:
        # 1. checks for a winning move for the computer player
        # it looks for a row, column or diagonal where the computer player has 2 out of 3 squares, and the third square is empty
        # then it returns that empty square to win the game

        # 2. if no winning move is found, then it gets the empty squares that are adjacent to the player's squares, if an empty square is next to a players square, then it puts that square in the list of possible moves (this is medium difficulty, that's why it doesn't check for the player's winning moves)
        # 3. return a random square from the list of possible moves
        pass

    def hard_move(self, game_board):
        # Implement a more advanced strategy here
        # Take the game board and:
        # 1. checks for a winning move for the computer player
        # it looks for a row, column or diagonal where the computer player has 2 out of 3 squares, and the third square is empty
        # then it returns that empty square to win the game

        # 2. checks for a winning move for the player
        # it looks for a row, column or diagonal where the player has 2 out of 3 squares, and the third square is empty
        # then it returns that empty square to block the player from winning the game, if there are 2 or more winning moves for the player, then it returns the first one it finds
        # 3. if no winning move is found, then it gets the empty squares that are adjacent to the player's squares, if an empty square is next to a players square, then it puts that square in the list of possible moves
        pass
