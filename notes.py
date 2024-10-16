When I click a game button in gameboard.py it runs this function:
def on_game_button_click(self, i, j):
        button = self.game_board_buttons[i * 3 + j]
        if self.players_turn == "X":
            button.configure(text="X", state="disabled", fg_color="darkred")
            self.players_turn = "O"
        else:
            button.configure(text="O", state="disabled", fg_color="darkgreen")
            self.players_turn = "X"

        self.master.menu_frame.on_button_click(i, j)

and the function in menu_frame.py is:
def on_button_click(self, i, j):
        self.click_counter += 1
        players_turn = self.players_turn.get()
        if players_turn == "X":
            self.players_turn_label.configure(text_color="green")
            self.set_matrix(i, j, "X")
            if self.check_if_winner(players_turn):
                self.winner(players_turn)
                return
            elif self.click_counter == 9:
                self.players_tie()
                return
            else:
                self.players_turn.set("O")
        else:
            self.players_turn_label.configure(text_color="red")
            self.set_matrix(i, j, "O")
            if self.check_if_winner(players_turn):
                self.winner(players_turn)
                return
            elif self.click_counter == 9:
                self.players_tie()
                return
            else:
                self.players_turn.set("X")
        self.players_turn_label.configure(
            text=f"Player {self.players_turn.get()}'s Turn"
        )

And the function players_tie runs this function in menu_frame.py:
    def players_tie(self):
        self.players_turn_label.configure(
            text="The Players have Tied!", text_color="Orange"
        )
        self.master.game_board.disable_board()
        self.game_counter()
        messagebox.showinfo(
            "Tie Game", "The Players have Tied!, Please start a new game!"
        )

My question is why does the messagebox pop up before the button has been configured with the text and color?