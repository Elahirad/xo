import pygame

from .menus import MainMenu, SubMenu
from .constants import WIDTH, HEIGHT, SQUARE_SIZE
from .managers import DisplayManager
from interfaces.user_interface import UserInterface


class PyGameUserInterface(UserInterface):
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("XO Game")
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__clock = pygame.time.Clock()
        self.__main_menu = MainMenu()
        self.__submenu = SubMenu()
        self.__display_manager = DisplayManager()
        self.__BACK_X_Y = (55, 47)
        self.__BACK_SHAPE = (200, 90)

    def submenu(self):
        return self.__submenu.show_submenu(self.__screen)
    
    def main_menu(self):
        return self.__main_menu.show_main_menu(self.__screen)
    
    def show_stats(self, x_wins, o_wins, turn):
        return self.__display_manager.draw_board(self.__screen, x_wins, o_wins, turn)
    
    def show_board(self, board):
        return self.__display_manager.draw_xo(board, self.__screen)
    
    def __check_back(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if mouseX in range(self.__BACK_X_Y[0], self.__BACK_X_Y[0] + self.__BACK_SHAPE[0]) and mouseY in range(self.__BACK_X_Y[1], self.__BACK_X_Y[1] + self.__BACK_SHAPE[1]):
                return True
        return False

    def event_handler(self, state):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'QUIT'

                if state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER', 'SUBMENU']:
                    if self.__check_back(event):
                        return 'MAIN_MENU'

                if state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER']:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseX = event.pos[0]
                        mouseY = event.pos[1]
                        if not (mouseX in range(114, 450) and mouseY in range(140, 476)):
                            return
                        mouseX -= 114
                        mouseY -= 140
                        clicked_row = int(mouseY // SQUARE_SIZE)
                        clicked_col = int(mouseX // SQUARE_SIZE)
                        return (clicked_row, clicked_col)
                if state == 'SUBMENU':
                    return self.__submenu.handle_mouse(event)
                if state == 'MAIN_MENU':
                    return self.__main_menu.handle_mouse(event)
                
    def update(self):
        pygame.display.update()
        self.__clock.tick(60)

    def exit(self):
        return pygame.quit()
