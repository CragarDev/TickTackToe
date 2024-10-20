import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class MenuFrameHvC(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # n-  Variables and frames ----------------------------------------------
        self.player_selection = tk.StringVar()
        self.selected_player = tk.StringVar()
        self.games_played = tk.IntVar(value=0)
        self.player_x_win_count = tk.IntVar(value=0)
        self.player_o_win_count = tk.IntVar(value=0)
        self.players_turn = tk.StringVar()
        self.click_counter = 0
        self.players_tied_count = tk.IntVar(value=0)
        self.game_over = False

        self.game_matrix_dict = {
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
        print(f"player_selection: {self.players_turn.get()}")
        print(f"selected_player: {self.selected_player.get()}")
        print(f"players_turn: {self.players_turn.get()}")
        print(f"gameboard_players_turn: ")
        print()
        # n- create labels, entry, and buttons and grid them ------------------------

        # New Game Button
        self.new_game_button = ctk.CTkButton(
            self,
            text="New Game",
            command=self.new_game,
            font=("Helvetica", 24, "bold"),
            fg_color="green",
            hover_color="dark green",
            corner_radius=20,
        )
        self.new_game_button.grid(
            row=0, column=0, rowspan=2, sticky="ew", padx=20, pady=20
        )

        # Quit Button
        # self.quit_button = ctk.CTkButton(
        #     self,
        #     text="Quit",
        #     command=self.quit,
        #     width=20,
        #     height=2,
        #     font=("Helvetica", 12, "bold"),
        #     bg="red",
        #     fg="white",
        #     hover_color="dark red",
        # )

        # self.quit_button.grid(row=1, column=0, sticky="nsew")

        # Player Selection Frame
        self.player_selection_frame = ctk.CTkFrame(self)

        self.player_selection_frame.grid(row=0, column=1, sticky="nsew")
        self.player_selection_frame.grid_columnconfigure((0), weight=3)
        self.player_selection_frame.grid_columnconfigure((1), weight=1)
        self.player_selection_frame.grid_rowconfigure((0), weight=1)

        # Player Selection Radio Buttons Frame
        self.player_selection_radio_frame = ctk.CTkFrame(self.player_selection_frame)
        self.player_selection_radio_frame.grid(row=0, column=1, sticky="nsew")
        self.player_selection_radio_frame.grid_columnconfigure((0, 1), weight=1)
        self.player_selection_radio_frame.grid_rowconfigure((0), weight=1)

        # Select Your Player Label
        self.select_your_player_label = ctk.CTkLabel(
            self.player_selection_frame,
            text="Select Player: ",
            text_color="white",
            font=("Helvetica", 20, "bold"),
        )
        self.select_your_player_label.grid(
            row=0, column=0, sticky="nsew", padx=20, pady=5
        )

        # Player Selection Radio Buttons
        self.player_x_radio = ctk.CTkRadioButton(
            self.player_selection_radio_frame,
            text="X",
            variable=self.player_selection,
            value="X",
            font=("Helvetica", 32, "bold"),
            text_color="white",
            text_color_disabled="white",
            fg_color="blue",
            hover_color="dark blue",
            border_color="blue",
            command=self.player_selected,
        )
        self.player_x_radio.grid(row=0, column=0, sticky="nsew", padx=5)

        self.player_o_radio = ctk.CTkRadioButton(
            self.player_selection_radio_frame,
            text="O",
            variable=self.player_selection,
            value="O",
            font=("Helvetica", 32, "bold"),
            text_color="white",
            text_color_disabled="white",
            fg_color="blue",
            hover_color="dark blue",
            border_color="blue",
            command=self.player_selected,
        )
        self.player_o_radio.grid(row=0, column=1, sticky="nsew", padx=5)

        # Games Played Frame
        self.games_played_frame = ctk.CTkFrame(self)
        self.games_played_frame.grid(row=0, column=2, sticky="nsew")
        self.games_played_frame.grid_columnconfigure((0), weight=3)
        self.games_played_frame.grid_columnconfigure((1), weight=1)
        self.games_played_frame.grid_rowconfigure((0), weight=1)

        # Games Played Label
        self.games_played_label = ctk.CTkLabel(
            self.games_played_frame,
            text="Games Played:",
            font=("Helvetica", 20, "bold"),
        )
        self.games_played_label.grid(row=0, column=0, sticky="e", padx=20, pady=5)

        # Games Played Entry
        self.games_played_count = ctk.CTkLabel(
            self.games_played_frame,
            font=("Helvetica", 32, "bold"),
            textvariable=self.games_played,
        )
        self.games_played_count.grid(row=0, column=1, sticky="w", padx=20, pady=5)

        # Winners Frame
        self.winners_frame = ctk.CTkFrame(self)
        self.winners_frame.grid(row=1, column=2, sticky="nsew")
        self.winners_frame.grid_columnconfigure((0), weight=3)
        self.winners_frame.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.winners_frame.grid_rowconfigure((0, 1), weight=1)

        # Winners Label
        self.winners_label = ctk.CTkLabel(
            self.winners_frame,
            text="Wins:",
            font=("Helvetica", 20, "bold"),
        )
        self.winners_label.grid(row=0, column=0, sticky="e", padx=20, pady=2)

        # Wins by players labels
        self.player_x_win_count_label = ctk.CTkLabel(
            self.winners_frame,
            text="X: ",
            text_color="red",
            font=("Helvetica", 20, "bold"),
        )
        self.player_x_win_count_label.grid(row=0, column=1, sticky="e", padx=10)

        self.player_x_win_counter = ctk.CTkLabel(
            self.winners_frame,
            text=self.player_x_win_count.get(),
            font=("Helvetica", 32, "bold"),
        )
        self.player_x_win_counter.grid(row=0, column=2, sticky="w", padx=10, pady=2)

        self.player_o_win_count_label = ctk.CTkLabel(
            self.winners_frame,
            text="O:",
            text_color="green",
            font=("Helvetica", 20, "bold"),
        )
        self.player_o_win_count_label.grid(row=0, column=3, sticky="e", padx=10)

        self.player_o_win_counter = ctk.CTkLabel(
            self.winners_frame,
            text=self.player_o_win_count.get(),
            font=("Helvetica", 32, "bold"),
        )
        self.player_o_win_counter.grid(row=0, column=4, sticky="w", padx=10, pady=2)

        self.tied_label = ctk.CTkLabel(
            self.winners_frame,
            text="Ties:",
            font=("Helvetica", 20, "bold"),
        )
        self.tied_label.grid(row=1, column=0, sticky="e", padx=20, pady=2)

        self.player_tied_counter = ctk.CTkLabel(
            self.winners_frame,
            text=self.players_tied_count.get(),
            font=("Helvetica", 32, "bold"),
        )
        self.player_tied_counter.grid(row=1, column=1, sticky="e", padx=10, pady=2)

        #  Players turn label -------------------------------
        self.players_turn_label = ctk.CTkLabel(
            self,
            text="Please select a player!",
            text_color="white",
            font=("Helvetica", 32, "bold"),
        )
        self.players_turn_label.grid(row=1, column=1, sticky="nsew")

        # n-  Methods -----------------------------------------------------------

    def new_game(self):
        print("%" * 50)
        print("--- Starting a New Game ---")
        print("%" * 50)
        print()

        self.player_x_radio.configure(
            state="normal",
            text_color="white",
            fg_color="blue",
            hover_color="dark blue",
            border_color="blue",
            hover=True,
            text_color_disabled="white",
        )
        self.player_o_radio.configure(
            state="normal",
            text_color="white",
            fg_color="blue",
            hover_color="dark blue",
            border_color="blue",
            hover=True,
            text_color_disabled="white",
        )
        # Call reset_board method in GameBoard instance
        self.master.game_board.reset_board()
        self.player_selection.set("")
        self.players_turn_label.configure(
            text_color="white", text="Please select a player!"
        )
        self.select_your_player_label.configure(
            text="--- Select Player ---", text_color="white"
        )
        # reset matrix
        self.reset_matrix()
        self.click_counter = 0

    def player_selected(self):
        print(
            f"New Starting Player Selected: {self.player_selection.get()} Starts the game"
        )
        print()
        if self.player_selection.get() == "X":
            self.player_o_radio.configure(
                state="disabled",
                text_color="gray20",
                fg_color="gray20",
                border_color="gray20",
                text_color_disabled="gray20",
            )
            self.player_x_radio.configure(
                state="disabled",
                text_color="red",
                text_color_disabled="red",
                fg_color="red",
                hover=False,
            )
            self.players_turn_label.configure(
                text_color="red", text=f"Player {self.player_selection.get()}'s Turn"
            )

        else:
            self.player_x_radio.configure(
                state="disabled",
                text_color="gray20",
                fg_color="gray20",
                text_color_disabled="gray20",
                border_color="gray20",
            )
            self.player_o_radio.configure(
                state="disabled",
                text_color="green",
                text_color_disabled="green",
                fg_color="green",
                hover=False,
            )
            self.players_turn_label.configure(
                text_color="green", text=f"Player {self.player_selection.get()}'s Turn"
            )

        # self.update_turn_label()
        self.select_your_player_label.configure(
            text="Player Selected", text_color="gray70"
        )
        self.master.game_board.enable_board(self.player_selection.get())

    def game_counter(self):
        self.games_played.set(self.games_played.get() + 1)

    def player_wins(self, player):
        if player == "X":
            self.player_x_win_count.set(self.player_x_win_count.get() + 1)
        else:
            self.player_o_win_count.set(self.player_o_win_count.get() + 1)
        self.players_turn_label.configure(text=f"Player {player} Wins")

    def on_button_click(self, i, j, player):
        self.click_counter += 1
        self.players_turn.set(player)
        print(f"Menu Frame - Game Button {i} {j} was clicked")
        print(f"Current Player: {self.players_turn.get()}")
        if self.players_turn.get() == "X":
            self.set_matrix(i, j, "X")
            if self.check_if_winner(self.players_turn.get()):
                print(
                    f"Checked, and Yes, Player {self.players_turn.get()} is the winner"
                )
                print()
                self.winner(self.players_turn.get())

            elif self.click_counter == 9:
                print("Yes, The Players have Tied!")
                self.players_tie()

            else:
                print(
                    f"Player {self.players_turn.get()} is not the winner and now it's O's turn"
                )
                # Set the next player
                self.players_turn_label.configure(text_color="green")
                self.players_turn.set("O")

        else:
            self.set_matrix(i, j, "O")
            if self.check_if_winner(self.players_turn.get()):
                print(
                    f"Checked, and Yes, Player {self.players_turn.get()} is the winner"
                )
                print()
                self.winner(self.players_turn.get())

            elif self.click_counter == 9:
                print("Yes, The Players have Tied!")
                self.players_tie()

            else:
                print(
                    f"Player {self.players_turn.get()} is not the winner and now it's X's turn"
                )
                self.players_turn_label.configure(text_color="red")
                self.players_turn.set("X")

        if self.game_over:
            return
        self.players_turn_label.configure(
            text=f"Player {self.players_turn.get()}'s Turn"
        )
        print(f"Next Player: {self.players_turn.get()}")
        print(
            f"--- Gameboard is waiting for player {self.players_turn.get()} to make a move ---"
        )
        print()
        print()
        return

        # self.game_counter()

    def update_turn_label(self):
        self.players_turn_label_content = f"Player {self.players_turn.get()}'s Turn"
        print()
        print("*" * 50)
        print(self.players_turn_label_content)
        print("*" * 50)
        print()

    def set_matrix(self, i, j, player):
        print(f"Setting Matrix: {i} {j}, {player}")
        # loop through the game_matrix_dict and set the player
        for key, value in self.game_matrix_dict.items():
            if value[0] == (i, j):
                self.game_matrix_dict[key][1] = True
                self.game_matrix_dict[key][2] = player

        self.print_matrix()

    def reset_matrix(self):
        for key, value in self.game_matrix_dict.items():
            self.game_matrix_dict[key][1] = False
            self.game_matrix_dict[key][2] = ""
        self.print_matrix()

    def print_matrix(self):
        # set up a print layout that is easy to read
        print()
        print("*" * 50)
        print("Game Matrix")
        counter = 1
        rows = []
        columns = []
        for key, value in self.game_matrix_dict.items():
            if value[1]:
                square_value = value[2]
            else:
                square_value = "-"
            # print(square_value)
            # print(f"Counter: {counter}")
            columns.append(square_value)
            if counter == 3 or counter == 6 or counter == 9:
                rows.append(columns)
                columns = []
            counter += 1

            # print(f"{key}: {value[2]}")
        for row in rows:
            print(row[0], row[1], row[2])
        print("*" * 50)
        print()

    def check_if_winner(self, player):
        print(f"Checking if player {player} is the winner")
        print(f"Click Counter: {self.click_counter}")
        for key, value in self.game_matrix_dict.items():
            if (
                self.game_matrix_dict.get("sq1")[2] == player
                and self.game_matrix_dict.get("sq2")[2] == player
                and self.game_matrix_dict.get("sq3")[2] == player
            ):
                return True
            elif (
                self.game_matrix_dict.get("sq4")[2] == player
                and self.game_matrix_dict.get("sq5")[2] == player
                and self.game_matrix_dict.get("sq6")[2] == player
            ):
                return True
            elif (
                self.game_matrix_dict.get("sq7")[2] == player
                and self.game_matrix_dict.get("sq8")[2] == player
                and self.game_matrix_dict.get("sq9")[2] == player
            ):
                return True
            elif (
                self.game_matrix_dict.get("sq1")[2] == player
                and self.game_matrix_dict.get("sq4")[2] == player
                and self.game_matrix_dict.get("sq7")[2] == player
            ):
                return True
            elif (
                self.game_matrix_dict.get("sq2")[2] == player
                and self.game_matrix_dict.get("sq5")[2] == player
                and self.game_matrix_dict.get("sq8")[2] == player
            ):
                return True
            elif (
                self.game_matrix_dict.get("sq3")[2] == player
                and self.game_matrix_dict.get("sq6")[2] == player
                and self.game_matrix_dict.get("sq9")[2] == player
            ):
                return True
            elif (
                self.game_matrix_dict.get("sq1")[2] == player
                and self.game_matrix_dict.get("sq5")[2] == player
                and self.game_matrix_dict.get("sq9")[2] == player
            ):
                return True
            elif (
                self.game_matrix_dict.get("sq3")[2] == player
                and self.game_matrix_dict.get("sq5")[2] == player
                and self.game_matrix_dict.get("sq7")[2] == player
            ):
                return True
            else:
                print("=" * 50)
                print("--- No Winner Yet ---")
                print("=" * 50)
                print()
                return False

    def winner(self, player):
        print("@" * 50)
        print("@" * 50)
        print(f"Winner... Winner... Chicken Dinner,\nPlayer {player} is the Winner")
        print("@" * 50)
        print("@" * 50)
        print()
        self.players_turn_label.configure(
            text=f"Player {player} is the Winner!", text_color="Orange"
        )
        self.game_counter()
        # disable the game board
        self.master.game_board.disable_board()

        if player == "X":
            self.player_x_win_count.set(self.player_x_win_count.get() + 1)
            print(f"Player X Win Count: {self.player_x_win_count.get()}")
            self.player_x_win_counter.configure(text=str(self.player_x_win_count.get()))

        else:
            self.player_o_win_count.set(self.player_o_win_count.get() + 1)
            print(f"Player O Win Count: {self.player_o_win_count.get()}")
            self.player_o_win_counter.configure(text=str(self.player_o_win_count.get()))

        self.players_turn_label.configure(text=f"Player {player} Wins")
        print("_" * 50)
        print("_" * 50)
        print("_" * 50)
        print()
        self.click_counter = 0
        self.game_over = True
        # Force the GUI to update
        self.master.update_idletasks()

        messagebox.showinfo(
            "Game Won",
            f"Congratulations!!! \nPlayer {player} Has Won The Game!, \nPlease start a new game!",
        )

    def players_tie(self):
        self.players_tied_count.set(self.players_tied_count.get() + 1)
        self.player_tied_counter.configure(text=self.players_tied_count.get())
        print("|" * 50)
        print("--- The Players have Tied the game! ---")
        print("|" * 50)
        self.players_turn_label.configure(
            text="The Players have Tied!", text_color="Orange"
        )
        self.master.game_board.disable_board()
        self.game_counter()

        # Force the GUI to update
        self.master.update_idletasks()

        messagebox.showinfo(
            "Tie Game", "The Players have Tied!, \nPlease start a new game!"
        )
