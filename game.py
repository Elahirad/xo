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
        self.state = 'MAIN_MENU'
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_manager = GameManager()
        self.ai = AI()
        self.running = True
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.x_wins = 0
        self.o_wins = 0
        self.player_flag = 1
        self.cpu_flag = 2
        self.turn = 1
        self.main_menu = MainMenu()
        self.submenu = SubMenu()
        self.board_manager = BoardManager()
        self.main_menu.show_main_menu(self.screen)
        self.BACK_X_Y = (55, 47)
        self.BACK_SHAPE = (200, 90)

    
    def clear_board(self) -> None:
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def clear_scores(self) -> None:
        self.x_wins = 0
        self.o_wins = 0

    def check_back(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if mouseX in range(self.BACK_X_Y[0], self.BACK_X_Y[0] + self.BACK_SHAPE[0]) and mouseY in range(self.BACK_X_Y[1], self.BACK_X_Y[1] + self.BACK_SHAPE[1]):
                self.state = 'MAIN_MENU'


    def event_handler(self) -> None:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if self.state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER', 'SUBMENU']:
                    self.check_back(event)

                if self.state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER']:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseX = event.pos[0]
                        mouseY = event.pos[1]
                        if not (mouseX in range(114, 450) and mouseY in range(140, 476)):
                            return
                        mouseX -= 114
                        mouseY -= 140
                        clicked_row = int(mouseY // SQUARE_SIZE)
                        clicked_col = int(mouseX // SQUARE_SIZE)
                        if self.state == 'PLAY_WITH_USER':
                            if self.board[clicked_row][clicked_col] == 0:
                                self.board[clicked_row][clicked_col] = self.turn
                                if self.turn == 1:
                                    self.turn = 2
                                elif self.turn == 2:
                                    self.turn = 1
                        else:
                            if self.turn == 1 and self.board[clicked_row][clicked_col] == 0:
                                self.board[clicked_row][clicked_col] = 1
                                self.turn = 2
                if self.state == 'SUBMENU':
                    opt = self.submenu.handle_mouse(event)
                    if opt == 'OPTION1':
                        self.state = 'PLAY_WITH_CPU'
                        self.clear_board()
                        self.clear_scores()
                        self.turn = 2
                    elif opt == 'OPTION2':
                        self.state = 'PLAY_WITH_CPU'
                        self.clear_board()
                        self.clear_scores()
                        self.turn = 1
                if self.state == 'MAIN_MENU':
                    opt = self.main_menu.handle_mouse(event)
                    if opt == 'OPTION1':
                        self.state = 'SUBMENU'
                        self.clear_board()
                        self.clear_scores()
                    elif opt == 'OPTION2':
                        self.state = 'PLAY_WITH_USER'
                        self.clear_board()
                        self.clear_scores()
                    elif opt == 'OPTION3':
                        self.state = 'EXIT'

    def handle_end(self) -> None:
        is_ended, winner = self.game_manager.check_win(self.board)
        if is_ended or self.game_manager.is_ended(self.board):
            if winner is None:
                self.clear_board()
                self.turn = randint(1, 2)
            else:
                if winner == 1:
                    self.x_wins += 1
                else:
                    self.o_wins += 1
                self.clear_board()
                self.turn = winner

    def launch_game(self) -> None:
        while self.running:
            if self.state == 'EXIT':
                break
            
            if self.state == 'MAIN_MENU':
                self.main_menu.show_main_menu(self.screen)

            if self.state == 'SUBMENU':
                self.submenu.show_submenu(self.screen)

            if self.state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER']:
                self.board_manager.draw_board(self.screen, self.x_wins, self.o_wins, self.turn)

            self.event_handler()
            
            if self.state == 'PLAY_WITH_CPU':
                self.handle_end()
                if self.turn == 2:
                    row, col = self.ai.move(self.board, self.cpu_flag)
                    self.board[row][col] = 2
                    self.turn = 1

                self.board_manager.draw_xo(self.board, self.screen)
                self.handle_end()

            if self.state == 'PLAY_WITH_USER':
                self.handle_end()

                self.board_manager.draw_xo(self.board, self.screen)

                self.handle_end()

            pygame.display.update()

            self.clock.tick(60)


        pygame.quit()
        