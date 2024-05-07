import pygame
from .constants import SQUARE_SIZE, WIDTH, HEIGHT

class DisplayManager:
    def __init__(self) -> None:
        self.__X_IMAGE = pygame.transform.scale(pygame.image.load("./interfaces/pygame_interface/images/x.png"), (100, 100))
        self.__O_IMAGE = pygame.transform.scale(pygame.image.load("./interfaces/pygame_interface/images/o.png"), (100, 100))
        self.__BG_IMAGE = pygame.transform.scale(pygame.image.load("./interfaces/pygame_interface/images/board.png"), (WIDTH, HEIGHT))
        self.__font = pygame.font.Font('freesansbold.ttf', 40)

    def __display_text(self, screen, text, x, y):
        text_surface = self.__font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (x, y))

    def draw_board(self, screen, x_wins, o_wins, turn):
        screen.blit(self.__BG_IMAGE, (0, 0))
        self.__display_text(screen, f"{x_wins}", 350, 485)
        self.__display_text(screen, f"{o_wins}", 155, 485)
        if turn == 1:
            pygame.draw.circle(screen, (255, 0, 0), (432, 502), 25, 3)
        else:
            pygame.draw.circle(screen, (255, 0, 0), (240, 502), 25, 3)

    def draw_xo(self, board, screen) -> None:
        for i in range(3):
            for j in range(3):
                x = j * SQUARE_SIZE * 0.95
                y = i * SQUARE_SIZE * 0.9
                if board[i][j] == 1:
                    screen.blit(self.__X_IMAGE, (x + 125, y + 160))
                if board[i][j] == 2:
                    screen.blit(self.__O_IMAGE, (x + 125, y + 160))