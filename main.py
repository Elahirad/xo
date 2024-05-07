from game import Game
from ai import AI
from managers import GameManager, BoardManager
from interfaces.pygame_interface.interface import PyGameUserInterface
from interfaces.terminal_interface.interface import TerminalUserInterface


if __name__ == '__main__':
    ai = AI()
    game_manager = GameManager()
    board_manager = BoardManager()
    # user_interface = PyGameUserInterface()
    user_interface = TerminalUserInterface()

    game = Game(game_manager, ai, board_manager, user_interface)
    game.launch_game()