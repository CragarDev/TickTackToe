import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class GameBoardHvC(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0), weight=1)

        # n-  Variables and frames ----------------------------------------------
        self.players_turn = tk.StringVar()
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
                    command=lambda i=i, j=j: self.on_game_button_click(i, j),
                )
                button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
                self.game_board_buttons.append(button)

        # n-  Methods -----------------------------------------------------------

    def on_game_button_click(self, i, j):

        # Get the players turn from the menu frame
        # players_turn = self.master.menu_frame.players_turn.get()
        print(
            f"Player {self.players_turn.get()} has clicked a button {i} {j} on the game board"
        )

        print()
        button = self.game_board_buttons[i * 3 + j]
        print(self.players_turn.get())
        if self.players_turn.get() == "X":
            button.configure(text="X", state="disabled", fg_color="darkred")
            # run a button click event in the menu frame from the app.py
            self.master.menu_frame_hvh.on_button_click(i, j, self.players_turn.get())
            self.players_turn.set(value="O")
        else:
            button.configure(text="O", state="disabled", fg_color="darkgreen")
            # run a button click event in the menu frame from the app.py
            self.master.menu_frame_hvh.on_button_click(i, j, self.players_turn.get())
            self.players_turn.set(value="X")
        # print(
        #     f"Gameboard is waiting for Player {self.players_turn.get()} to click a button"
        # )
        # Force the GUI to update
        self.master.update_idletasks()

    def reset_board(self):
        for button in self.game_board_buttons:
            button.configure(state="disabled", text=" ", fg_color="gray40")
        # self.master.menu_frame.reset_game()

    def enable_board(self, selected_player):
        self.players_turn.set(selected_player)
        print(f"--- Enabling board ---")
        print(f"Current Player: {self.players_turn.get()}")
        for button in self.game_board_buttons:
            button.configure(state="normal")

        print(
            f"--- Gameboard - Waiting for player {self.players_turn.get()} to make a move ---"
        )
        print()

    def disable_board(self):
        for button in self.game_board_buttons:
            button.configure(state="disabled")
