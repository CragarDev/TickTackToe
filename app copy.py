import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

from menu_frame import MenuFrame
from gameboard import GameBoard


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        print()
        print("⦿" * 50)
        print("     Welcome to Tick Tack Toe")
        print("⦿" * 50)
        print()

        # System settings
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # geometry
        self.title("Tick Tack Toe")
        self.geometry("1000x1000+1200+500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)

        # Start the game
        # Start button
        self.start_button = ctk.CTkButton(
            self,
            text="Start the Game of Tick Tack Toe",
            command=self.start_game,
            font=("Helvetica", 24, "bold"),
            fg_color="#194ca9",
            hover_color="#113679",
            corner_radius=20,
            height=50,
        )
        self.start_button.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=180,
            pady=10,
            rowspan=2,
        )

        # import the MenuFrame class
        self.menu_frame = MenuFrame(self)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.menu_frame.grid_forget()

        # grid the game board frame
        self.game_board = GameBoard(self)
        self.game_board.grid(row=1, column=0, sticky="nsew")
        self.game_board.grid_forget()

        # Bind the close event to the on_closing method
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        print()
        print("◆" * 50)
        print("       Tick Tack Toe App has closed")
        print("◆" * 50)
        print()
        self.quit()

    def start_game(self):
        self.start_button.grid_forget()
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.game_board.grid(row=1, column=0, sticky="nsew")
        print("The game of 'Tick Tack Toe' has begun!")
        print()
        self.menu_frame.new_game()
