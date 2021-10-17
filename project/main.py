import os


class TicTacToe:
    def __init__(self) -> None:
        self.x_score = 0
        self.o_score = 0
        self.x_selected = []
        self.o_selected = []
        self.spaces_available = self.get_clean_availables()
        self.board = self.get_clean_board()
        self.is_on = True
        self.set_running = False
        self.is_x_turn = True
        self.winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [6, 4, 2],
        ]

    def pretty_board(self):
        return f"""
\t   {self.board[0]}   |   {self.board[1]}   |   {self.board[2]}   
\t-------+-------+-------
\t   {self.board[3]}   |   {self.board[4]}   |   {self.board[5]}   
\t-------+-------+-------
\t   {self.board[6]}   |   {self.board[7]}   |   {self.board[8]}   

"""

    def get_clean_board(self) -> list:
        return [str(x) for x in range(9)]

    def get_clean_availables(self):
        return [x for x in range(9)]

    def play_turn(self):
        print(f"It is {'X' if self.is_x_turn else 'O'}'s turn")

        # Check if user picked spot is valid or ask again if its not
        right_selection = False
        while not right_selection:
            selection = input(
                f"Select one of the available spaces({self.spaces_available}):"
            )
            try:
                selection_int = int(selection)
            except ValueError:
                print("Your input is not an integer, please try again.")
            else:
                right_selection = self.validate_selection(selection_int)
                if not right_selection:
                    print("Number not available, try another one.")

        # Place selection in board and list
        self.add_to_selected(selection_int)

        # Check if we have a winner
        if self.check_if_winner():
            print(self.pretty_board())
            self.set_running = False

        # Change turns
        self.is_x_turn = not self.is_x_turn

    def clear_score(self):
        self.x_score = 0
        self.o_score = 0
        print("Score cleared!")

    def validate_selection(self, selection: int):
        if selection in self.spaces_available:
            return True
        return False

    def add_to_selected(self, selected: int):
        # Remove from available list
        self.spaces_available.remove(selected)

        # Add to current player list and board
        if self.is_x_turn:
            self.x_selected.append(selected)
            self.board[selected] = "X"
        else:
            self.o_selected.append(selected)
            self.board[selected] = "O"

    def check_if_winner(self):
        if self.is_x_turn:
            player_list = self.x_selected
        else:
            player_list = self.o_selected
        for win_set in self.winning_combinations:
            coincident = set(win_set).intersection(player_list)
            # print(coincident)
            if len(coincident) == 3:
                print("We got a winning combination!")
                if self.is_x_turn:
                    print("X wins this time!")
                    self.x_score += 1
                else:
                    print("O wins this time!")
                    self.o_score += 1
                return True
        if len(self.spaces_available) == 0:
            print("It's a DRAW!")
            return True
        return False

    def prepare_new_game(self):
        self.x_selected = []
        self.o_selected = []
        self.spaces_available = self.get_clean_availables()
        self.board = self.get_clean_board()


if __name__ == "__main__":
    print("\nHello and welcome to the tic.tac.toe game :)\n")

    game = TicTacToe()

    while game.is_on:
        print(f"Current score: X({game.x_score}) - O({game.o_score})")
        user_selection = input(
            "Press enter for new game, type 'clear' to clear the score, type 'q' to quit the game:"
        ).lower()
        if user_selection == "clear":
            game.clear_score()
        elif user_selection == "q":
            print("I hope you had fun, goodbye!")
            game.is_on = False
            break
        else:
            game.prepare_new_game()
            game.set_running = True
        while game.set_running:
            os.system("cls" if os.name == "nt" else "clear")
            print("TIC TAC TOE")
            print("Current board:\n")
            print(game.pretty_board())
            game.play_turn()
