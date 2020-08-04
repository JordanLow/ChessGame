from chess import Board, King, Queen, Bishop, Knight, Rook, Pawn
import curses

class TextInterface:
    def __init__(self):
        y, x = 0, 0
        self.boardwin = curses.initscr()
        self.msgwin = curses.initscr()
        self.inputwin = curses.initscr()
        self.boardwin = curses.newwin(11, 40, y, x)
        y += 11
        self.msgwin = curses.newwin(5, 40, y, x)
        y += 5
        self.inputwin = curses.newwin(3, 40, y, x)


    def set_board(self, inputstr):
        '''
        Takes board info as an inputstr
        and prints it to the console.
        '''
        self.boardwin.addstr(0, 0, inputstr)
        self.boardwin.refresh()

    def set_msg(self, inputstr, y=0, x=0):
        '''
        Takes an inputstr and prints it
        to the console.
        '''
        self.msgwin.addstr(x, y, inputstr)
        self.msgwin.refresh()

    def get_player_input(self, msgstr):
        '''
        Prompts the user with a msgstr,
        returns their input as str.
        '''
        self.inputwin.clear()
        self.inputwin.addstr(0, 0, msgstr)
        value = self.inputwin.getstr().decode('UTF-8')
        self.inputwin.refresh()
        return value

ui = TextInterface()
game = Board(inputf=ui.get_player_input, printf=ui.set_msg)

game.start()
while game.winner is None:
    ui.set_board(game.display())
    while True:
        start, end = game.prompt()
        ui.msgwin.clear()
        if game.valid_move(start, end):
            break
        else:
            ui.set_msg(f'Invalid move: {start} -> {end}')
    ui.set_msg(game.format_move(start, end))
    game.update(start, end)
    game.next_turn()
ui.set_msg(f'Game over. {game.winner()} player wins!')
