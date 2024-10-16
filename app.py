import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


from menu_frame_hvh import MenuFrameHvH
from menu_frame_hvc import MenuFrameHvC
from menu_frame_cvc import MenuFrameCvC
from gameboard_hvh import GameBoardHvH
from gameboard_hvc import GameBoardHvC
from gameboard_cvc import GameBoardCvC


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
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(3, weight=6)

        # Start the game
        # Start button - human vs human
        self.start_button_hvh = ctk.CTkButton(
            self,
            text="Human vs Human\nStart the Game of Tick Tack Toe",
            command=lambda: self.start_game("hvh"),
            font=("Helvetica", 24, "bold"),
            fg_color="#194ca9",
            hover_color="#113679",
            corner_radius=20,
            height=80,
        )
        self.start_button_hvh.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=180,
            pady=10,
        )
        # Start button - human vs computer
        self.start_button_hvc = ctk.CTkButton(
            self,
            text="Human vs Computer\nStart the Game of Tick Tack Toe",
            command=lambda: self.start_game("hvc"),
            font=("Helvetica", 24, "bold"),
            fg_color="#194ca9",
            hover_color="#113679",
            corner_radius=20,
            height=80,
        )
        self.start_button_hvc.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=180,
            pady=10,
        )
        # Start button - computer vs computer
        self.start_button_cvc = ctk.CTkButton(
            self,
            text="Computer vs Computer\nStart the Game of Tick Tack Toe",
            command=lambda: self.start_game("cvc"),
            font=("Helvetica", 24, "bold"),
            fg_color="#194ca9",
            hover_color="#113679",
            corner_radius=20,
            height=80,
        )
        self.start_button_cvc.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=180,
            pady=10,
        )

        # Force the GUI to update
        self.update_idletasks()

        # Bind the close event to the on_closing method
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        print()
        print("◆" * 50)
        print("       Tick Tack Toe App has closed")
        print("◆" * 50)
        print()
        self.quit()

    def start_game(self, game_type):
        print(f"game_type: {game_type}")
        # reset the self row grid
        self.start_button_hvh.grid_forget()
        self.start_button_hvc.grid_forget()
        self.start_button_cvc.grid_forget()

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)

        if game_type == "hvh":
            # grid the game board frame
            self.game_board_hvh = GameBoardHvH(self)
            self.game_board_hvh.grid(row=1, column=0, sticky="nsew")
            # import the MenuFrame hvh class
            self.menu_frame_hvh = MenuFrameHvH(self)
            self.menu_frame_hvh.grid(row=0, column=0, sticky="nsew")
            self.menu_frame_hvh.grid(row=0, column=0, sticky="nsew")
        elif game_type == "hvc":
            # grid the game board frame
            self.game_board_hvc = GameBoardHvC(self)
            self.game_board_hvc.grid(row=1, column=0, sticky="nsew")
            # import the MenuFrame hvc class
            self.menu_frame_hvc = MenuFrameHvC(self)
            self.menu_frame_hvc.grid(row=0, column=0, sticky="nsew")
            self.menu_frame_hvc.grid(row=0, column=0, sticky="nsew")
            self.menu_frame_hvc.new_game()
        elif game_type == "cvc":
            # grid the game board frame
            self.game_board_cvc = GameBoardCvC(self)
            self.game_board_cvc.grid(row=1, column=0, sticky="nsew")
            # import the MenuFrame cvc class
            self.menu_frame_cvc = MenuFrameCvC(self)
            self.menu_frame_cvc.grid(row=0, column=0, sticky="nsew")
            self.menu_frame_cvc.grid(row=0, column=0, sticky="nsew")
            self.menu_frame_cvc.new_game()
        print()
        print("The game of 'Tick Tack Toe' has begun!")
        print()
        if game_type == "hvh":
            print(f"Game Type: Human vs Human")
            self.menu_frame_hvh.new_game()
        elif game_type == "hvc":
            print(f"Game Type: Human vs Computer")
            self.menu_frame_hvc.new_game()
        elif game_type == "cvc":
            print(f"Game Type: Computer vs Computer")
            self.menu_frame_cvc.new_game()
