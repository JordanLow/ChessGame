from chess import Board, King, Queen, Bishop, Knight, Rook, Pawn
import curses

class ConsoleInterface:
    def __init__(self):
        pass

    def set_board(self, inputstr):
        '''
        Takes board info as an inputstr
        and prints it to the console.
        '''
        print(inputstr)
        return None

    def set_msg(self, inputstr):
        '''
        Takes an inputstr and prints it
        to the console.
        '''
        print(inputstr)
        return None

    def get_player_input(self, msgstr):
        '''
        Prompts the user with a msgstr,
        returns their input as str.
        '''
        value = input(msgstr)
        return value

ui = ConsoleInterface()
game = Board(inputf=ui.get_player_input, printf=ui.set_msg)

game.start()
while game.winner is None:
    ui.set_board(game.display())
    while True:
        start, end = game.prompt()
        if game.valid_move(start, end):
            break
        else:
            ui.set_msg(f'Invalid move: {start} -> {end}')
    ui.set_msg(game.format_move(start, end))
    game.update(start, end)
    game.next_turn()
ui.set_msg(f'Game over. {game.winner()} player wins!')
