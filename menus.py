import pygame

from constants import WIDTH, HEIGHT

class MainMenu:
    def __init__(self) -> None:
        self.MAIN_MENU_BG = pygame.transform.scale(pygame.image.load("images/main_menu.png"), (WIDTH, HEIGHT))
        self.OPTION1_SHAPE = (446, 69)
        self.OPTION2_SHAPE = (456, 77)
        self.OPTION3_SHAPE = (302, 72)
        self.OPTION1_X_Y = (70, 200)
        self.OPTION2_X_Y = (70, 290)
        self.OPTION3_X_Y = (150, 380)
    
    def show_main_menu(self, screen):
        screen.blit(self.MAIN_MENU_BG, (0, 0))

    def handle_mouse(self, event: pygame.event.EventType):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            if mouseX in range(self.OPTION1_X_Y[0], self.OPTION1_X_Y[0] + self.OPTION1_SHAPE[0]) and mouseY in range(self.OPTION1_X_Y[1], self.OPTION1_X_Y[1] + self.OPTION1_SHAPE[1]):
                return "OPTION1"
            elif mouseX in range(self.OPTION2_X_Y[0], self.OPTION2_X_Y[0] + self.OPTION1_SHAPE[0]) and mouseY in range(self.OPTION2_X_Y[1], self.OPTION2_X_Y[1] + self.OPTION2_SHAPE[1]):
                return "OPTION2"
            elif mouseX in range(self.OPTION3_X_Y[0], self.OPTION3_X_Y[0] + self.OPTION3_SHAPE[0]) and mouseY in range(self.OPTION3_X_Y[1], self.OPTION3_X_Y[1] + self.OPTION3_SHAPE[1]):
                return "OPTION3"
            else:
                return None
            

class SubMenu:
    def __init__(self) -> None:
        self.MAIN_MENU_BG = pygame.transform.scale(pygame.image.load("images/submenu.png"), (WIDTH, HEIGHT))
        self.OPTION1_SHAPE = (312, 80)
        self.OPTION2_SHAPE = (312, 80)
        self.OPTION1_X_Y = (150, 285)
        self.OPTION2_X_Y = (150, 382)
    
    def show_submenu(self, screen):
        screen.blit(self.MAIN_MENU_BG, (0, 0))

    def handle_mouse(self, event: pygame.event.EventType):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            if mouseX in range(self.OPTION1_X_Y[0], self.OPTION1_X_Y[0] + self.OPTION1_SHAPE[0]) and mouseY in range(self.OPTION1_X_Y[1], self.OPTION1_X_Y[1] + self.OPTION1_SHAPE[1]):
                return "OPTION1"
            elif mouseX in range(self.OPTION2_X_Y[0], self.OPTION2_X_Y[0] + self.OPTION1_SHAPE[0]) and mouseY in range(self.OPTION2_X_Y[1], self.OPTION2_X_Y[1] + self.OPTION2_SHAPE[1]):
                return "OPTION2"
            else:
                return None