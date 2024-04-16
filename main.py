from game import Game
from ai import AI
from managers import GameManager, BoardManager


if __name__ == '__main__':
    ai = AI()
    game_manager = GameManager()
    board_manager = BoardManager()
    game = Game(game_manager, ai, board_manager)
    game.launch_game()