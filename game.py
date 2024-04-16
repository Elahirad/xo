import pygame
from random import randint

from constants import HEIGHT, WIDTH, SQUARE_SIZE
from menus import MainMenu, SubMenu
from ai import AI
from managers import GameManager, BoardManager

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("XO Game")
        self.__state = 'MAIN_MENU'
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__clock = pygame.time.Clock()
        self.__game_manager = GameManager()
        self.__ai = AI()
        self.__running = True
        self.__board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__x_wins = 0
        self.__o_wins = 0
        self.__player_flag = 1
        self.__cpu_flag = 2
        self.__turn = 1
        self.__main_menu = MainMenu()
        self.__submenu = SubMenu()
        self.__board_manager = BoardManager()
        self.__main_menu.show_main_menu(self.__screen)
        self.__BACK_X_Y = (55, 47)
        self.__BACK_SHAPE = (200, 90)

    
    def __clear_board(self) -> None:
        self.__board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __clear_scores(self) -> None:
        self.__x_wins = 0
        self.__o_wins = 0

    def __check_back(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if mouseX in range(self.__BACK_X_Y[0], self.__BACK_X_Y[0] + self.__BACK_SHAPE[0]) and mouseY in range(self.__BACK_X_Y[1], self.__BACK_X_Y[1] + self.__BACK_SHAPE[1]):
                self.__state = 'MAIN_MENU'


    def __event_handler(self) -> None:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False

                if self.__state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER', 'SUBMENU']:
                    self.__check_back(event)

                if self.__state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER']:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseX = event.pos[0]
                        mouseY = event.pos[1]
                        if not (mouseX in range(114, 450) and mouseY in range(140, 476)):
                            return
                        mouseX -= 114
                        mouseY -= 140
                        clicked_row = int(mouseY // SQUARE_SIZE)
                        clicked_col = int(mouseX // SQUARE_SIZE)
                        if self.__state == 'PLAY_WITH_USER':
                            if self.__board[clicked_row][clicked_col] == 0:
                                self.__board[clicked_row][clicked_col] = self.__turn
                                if self.__turn == 1:
                                    self.__turn = 2
                                elif self.__turn == 2:
                                    self.__turn = 1
                        else:
                            if self.__turn == 1 and self.__board[clicked_row][clicked_col] == 0:
                                self.__board[clicked_row][clicked_col] = 1
                                self.__turn = 2
                if self.__state == 'SUBMENU':
                    opt = self.__submenu.handle_mouse(event)
                    if opt == 'OPTION1':
                        self.__state = 'PLAY_WITH_CPU'
                        self.__clear_board()
                        self.__clear_scores()
                        self.__turn = 2
                    elif opt == 'OPTION2':
                        self.__state = 'PLAY_WITH_CPU'
                        self.__clear_board()
                        self.__clear_scores()
                        self.__turn = 1
                if self.__state == 'MAIN_MENU':
                    opt = self.__main_menu.handle_mouse(event)
                    if opt == 'OPTION1':
                        self.__state = 'SUBMENU'
                        self.__clear_board()
                        self.__clear_scores()
                    elif opt == 'OPTION2':
                        self.__state = 'PLAY_WITH_USER'
                        self.__clear_board()
                        self.__clear_scores()
                    elif opt == 'OPTION3':
                        self.__state = 'EXIT'

    def __handle_end(self) -> None:
        is_ended, winner = self.__game_manager.check_win(self.__board)
        if is_ended or self.__game_manager.is_ended(self.__board):
            if winner is None:
                self.__clear_board()
                self.__turn = randint(1, 2)
            else:
                if winner == 1:
                    self.__x_wins += 1
                else:
                    self.__o_wins += 1
                self.__clear_board()
                self.__turn = winner

    def launch_game(self) -> None:
        while self.__running:
            if self.__state == 'EXIT':
                break
            
            if self.__state == 'MAIN_MENU':
                self.__main_menu.show_main_menu(self.__screen)

            if self.__state == 'SUBMENU':
                self.__submenu.show_submenu(self.__screen)

            if self.__state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER']:
                self.__board_manager.draw_board(self.__screen, self.__x_wins, self.__o_wins, self.__turn)

            self.__event_handler()
            
            if self.__state == 'PLAY_WITH_CPU':
                self.__handle_end()
                if self.__turn == 2:
                    row, col = self.__ai.move(self.__board, self.__cpu_flag)
                    self.__board[row][col] = 2
                    self.__turn = 1

                self.__board_manager.draw_xo(self.__board, self.__screen)
                self.__handle_end()

            if self.__state == 'PLAY_WITH_USER':
                self.__handle_end()

                self.__board_manager.draw_xo(self.__board, self.__screen)

                self.__handle_end()

            pygame.display.update()

            self.__clock.tick(60)


        pygame.quit()
        