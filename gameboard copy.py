import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class GameBoard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0), weight=1)

        # n-  Variables and frames ----------------------------------------------

        # n- create labels, entry, and buttons and grid them ------------------------

        # Game Board Frame
        self.game_board_frame = ctk.CTkFrame(self)
        self.game_board_frame.grid(row=0, column=0, sticky="nsew")
        self.game_board_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.game_board_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Game Board Buttons
        self.game_board_buttons = []
        for i in range(3):
            for j in range(3):
                button = ctk.CTkButton(
                    self.game_board_frame,
                    text=" ",
                    text_color="white",
                    font=("Helvetica", 84, "bold"),
                    fg_color="gray40",
                    hover_color="gray20",
                    state="disabled",
                    corner_radius=10,
                    command=lambda i=i, j=j: self.on_button_click(i, j),
                )
                button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
                self.game_board_buttons.append(button)

        # n-  Methods -----------------------------------------------------------

    def on_button_click(self, i, j):

        # Get the players turn from the menu frame
        # players_turn = self.master.menu_frame.players_turn.get()
        print(f"Player's Turn: {self.players_turn}")

        print(f"Button {i} {j} clicked")
        button = self.game_board_buttons[i * 3 + j]
        if self.players_turn == "X":
            button.configure(text="X", state="disabled", fg_color="darkred")
            self.players_turn = "O"
        else:
            button.configure(text="O", state="disabled", fg_color="darkgreen")
            self.players_turn = "X"

        # run a button click event in the menu frame from the app.py
        self.master.menu_frame.on_button_click(i, j)

    def reset_board(self):
        for button in self.game_board_buttons:
            button.configure(state="disabled", text=" ", fg_color="gray40")
        # self.master.menu_frame.reset_game()

    def enable_board(self, selected_player):
        self.players_turn = selected_player
        for button in self.game_board_buttons:
            button.configure(state="normal")
