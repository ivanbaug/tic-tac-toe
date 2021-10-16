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
   {self.board[0]}   |   {self.board[1]}   |   {self.board[2]}   
-------+-------+-------
   {self.board[3]}   |   {self.board[4]}   |   {self.board[5]}   
-------+-------+-------
   {self.board[6]}   |   {self.board[7]}   |   {self.board[8]}   

"""

    def get_clean_board(self) -> list:
        return [str(x) for x in range(9)]

    def get_clean_availables(self):
        return [x for x in range(9)]

    def play_turn(self):
        print(f"It is {'X' if self.is_x_turn else 'O'}'s turn")
        right_selection = False
        selection = input(
            f"Select one of the available spaces({self.spaces_available}):"
        )
        print(selection)

    def clear_score(self):
        self.x_score = 0
        self.o_score = 0
        print("Score cleared!")


if __name__ == "__main__":
    print("Hello and welcome to the tic.tac.toe game :)\n")

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
            game.set_running = True
        while game.set_running:
            print(game.pretty_board())
            game.set_running = False
            game.play_turn()
