from random import randint

from ai import AiInterface
from managers import GameManagerInterface, BoardManagerInterface
from interfaces.user_interface import UserInterface

class Game:
    def __init__(self, game_manager: GameManagerInterface, ai: AiInterface, board_manager: BoardManagerInterface, user_interface: UserInterface) -> None:
        
        self.__state = 'MAIN_MENU'
        self.__game_manager = game_manager
        self.__ai = ai
        self.__board_manager = board_manager
        self.__running = True
        self.__player_flag = 1
        self.__cpu_flag = 2
        self.__turn = 1
        self.__user_interface = user_interface

    def __event_handler(self) -> None:
        next_state = self.__user_interface.event_handler(self.__state)
        if next_state == 'QUIT':
            self.__running = False

        if next_state == 'MAIN_MENU':
            self.__state = 'MAIN_MENU'

        if self.__state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER'] and isinstance(next_state, tuple):
            clicked_row, clicked_col = next_state
            if self.__state == 'PLAY_WITH_USER':
                if self.__board_manager.board[clicked_row][clicked_col] == 0:
                    self.__board_manager.board[clicked_row][clicked_col] = self.__turn
                    if self.__turn == 1:
                        self.__turn = 2
                    elif self.__turn == 2:
                        self.__turn = 1
            else:
                if self.__turn == 1 and self.__board_manager.board[clicked_row][clicked_col] == 0:
                    self.__board_manager.board[clicked_row][clicked_col] = 1
                    self.__turn = 2
        if self.__state == 'SUBMENU':
            self.__board_manager.clear_board()
            self.__board_manager.clear_scores()
            opt = next_state
            if opt == 'OPTION1':
                self.__state = 'PLAY_WITH_CPU'
                self.__turn = 2
            elif opt == 'OPTION2':
                self.__state = 'PLAY_WITH_CPU'
                self.__turn = 1
        if self.__state == 'MAIN_MENU':
            self.__board_manager.clear_board()
            self.__board_manager.clear_scores()
            opt = next_state
            if opt == 'OPTION1':
                self.__state = 'SUBMENU'
            elif opt == 'OPTION2':
                self.__state = 'PLAY_WITH_USER'
            elif opt == 'OPTION3':
                self.__state = 'EXIT'

    def __handle_end(self) -> None:
        is_ended, winner = self.__game_manager.check_win(self.__board_manager.board)
        if is_ended or self.__game_manager.is_ended(self.__board_manager.board):
            if winner is None:
                self.__board_manager.clear_board()
                self.__turn = randint(1, 2)
            else:
                if winner == 1:
                    self.__board_manager.x_wins += 1
                else:
                    self.__board_manager.o_wins += 1
                self.__board_manager.clear_board()
                self.__turn = winner

    def launch_game(self) -> None:
        while self.__running:
            if self.__state == 'EXIT':
                break
            
            if self.__state == 'MAIN_MENU':
                self.__user_interface.main_menu()

            if self.__state == 'SUBMENU':
                self.__user_interface.submenu()

            if self.__state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER']:
                self.__user_interface.show_stats(self.__board_manager.x_wins, self.__board_manager.o_wins, self.__turn)

            
            if self.__state == 'PLAY_WITH_CPU':
                self.__handle_end()
                if self.__turn == 2:
                    row, col = self.__ai.move(self.__board_manager.board, self.__cpu_flag)
                    self.__board_manager.board[row][col] = 2
                    self.__turn = 1

                self.__user_interface.show_board(self.__board_manager.board)
                self.__handle_end()

            if self.__state == 'PLAY_WITH_USER':
                self.__handle_end()

                self.__user_interface.show_board(self.__board_manager.board)

                self.__handle_end()
            if self.__state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER']:
                self.__user_interface.show_stats(self.__board_manager.x_wins, self.__board_manager.o_wins, self.__turn)
                self.__user_interface.show_board(self.__board_manager.board)

            self.__event_handler()
            self.__user_interface.update()


        self.__user_interface.exit()
        