import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class MenuFrame(ctk.CTkFrame):
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
        self.players_turn = tk.StringVar(value="X")

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
            text="Games Played",
            font=("Helvetica", 20, "bold"),
        )
        self.games_played_label.grid(row=0, column=0, sticky="e", padx=20, pady=5)

        # Games Played Entry
        self.games_played_count = ctk.CTkLabel(
            self.games_played_frame,
            font=("Helvetica", 20, "bold"),
            textvariable=self.games_played,
        )
        self.games_played_count.grid(row=0, column=1, sticky="w", padx=20, pady=5)

        # Winners Frame
        self.winners_frame = ctk.CTkFrame(self)
        self.winners_frame.grid(row=1, column=2, sticky="nsew")
        self.winners_frame.grid_columnconfigure((0), weight=3)
        self.winners_frame.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.winners_frame.grid_rowconfigure((0), weight=1)

        # Winners Label
        self.winners_label = ctk.CTkLabel(
            self.winners_frame,
            text="Winners :",
            font=("Helvetica", 20, "bold"),
        )
        self.winners_label.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)

        # Wins by players labels
        self.player_x_win_count_label = ctk.CTkLabel(
            self.winners_frame,
            text="X: ",
            font=("Helvetica", 20, "bold"),
        )
        self.player_x_win_count_label.grid(row=0, column=1, sticky="e", padx=5)

        self.player_x_win_count = ctk.CTkLabel(
            self.winners_frame,
            textvariable=self.player_x_win_count,
            font=("Helvetica", 20, "bold"),
        )
        self.player_x_win_count.grid(row=0, column=2, sticky="w", padx=10)

        self.player_o_win_count_label = ctk.CTkLabel(
            self.winners_frame,
            text="O: ",
            font=("Helvetica", 20, "bold"),
        )
        self.player_o_win_count_label.grid(row=0, column=3, sticky="e", padx=5)

        self.player_o_win_count = ctk.CTkLabel(
            self.winners_frame,
            textvariable=self.player_o_win_count,
            font=("Helvetica", 20, "bold"),
        )
        self.player_o_win_count.grid(row=0, column=4, sticky="w", padx=10)

        # Players turn label
        self.players_turn_label = ctk.CTkLabel(
            self,
            text="Please select a player!",
            text_color="white",
            font=("Helvetica", 32, "bold"),
        )
        self.players_turn_label.grid(row=1, column=1, sticky="nsew")

        # n-  Methods -----------------------------------------------------------

    def new_game(self):
        print("New Game")

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

    def player_selected(self):
        print(f"Player Selected: {self.player_selection.get()}")
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

        self.master.game_board.enable_board(self.player_selection.get())

    def game_counter(self):
        self.games_played.set(self.games_played.get() + 1)

    def player_wins(self, player):
        if player == "X":
            self.player_x_win_count.set(self.player_x_win_count.get() + 1)
        else:
            self.player_o_win_count.set(self.player_o_win_count.get() + 1)
        self.players_turn_label.configure(text=f"Player {player} Wins")

    def on_button_click(self, i, j):
        print(f"Menu Frame Button {i} {j} clicked")
        players_turn = self.players_turn.get()
        if players_turn == "X":
            self.players_turn_label.configure(text_color="green")
            self.players_turn.set("O")
        else:
            self.players_turn_label.configure(text_color="red")
            self.players_turn.set("X")
        self.players_turn_label.configure(
            text=f"Player {self.players_turn.get()}'s Turn"
        )
        # self.game_counter()
        # self.check_winner()

    def update_turn_label(self):
        self.players_turn_label_content = f"Player {self.players_turn.get()}'s Turn"
        print()
        print("*" * 50)
        print(self.players_turn_label_content)
        print("*" * 50)
        print()
