from abc import ABC, abstractmethod

class UserInterface(ABC):

    @abstractmethod
    def submenu(self):
        pass
    
    @abstractmethod
    def main_menu(self):
        pass
    
    @abstractmethod
    def show_stats(self, x_wins, o_wins, turn):
        pass
    
    @abstractmethod
    def show_board(self, board):
        pass

    @abstractmethod
    def event_handler(self, state):
        pass

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def exit(self):
        pass
