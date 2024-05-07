from os import system
import platform
from interfaces.user_interface import UserInterface

class Utils:
    def clear_screen():
        if platform.system() == "Windows":
            system("cls")  # cls for windows
        else:
            system("clear")  # clear for other OS

class TerminalUserInterface(UserInterface):
    def __init__(self) -> None:
        pass

    def submenu(self):
        Utils.clear_screen()
        print("Play with Computer - Who plays first ?")
        menu = "1) Computer\n2) Player\n3) Back"
        print(menu)
    
    def main_menu(self):
        Utils.clear_screen()
        print("XO Game - Ali Elahirad 9918773")
        menu = "1) Play with Computer\n2) Play with another Player\n3) Exit"
        print(menu)
        
    
    def show_stats(self, x_wins, o_wins, turn):
        mapping = {1: 'X', 2: 'O'}
        Utils.clear_screen()
        print(f"X Wins: {x_wins} \t\t O Wins: {o_wins}")
        print(f"It's {mapping[turn]}'s turn")
    
    def show_board(self, board):
        print("   1  2  3")
        for i in range(3):
            print(f"{i + 1} ", end="")
            for j in range(3):
                if board[i][j] == 0:
                    xo = "-"
                elif board[i][j] == 1:
                    xo = "X"
                else:
                    xo = "O"
                print(f" {xo} ", end="")
            print()

    def event_handler(self, state):
        if state == 'MAIN_MENU':
            choice = ''
            while not choice in ['1', '2', '3']:
                choice = input("Enter your choice: ")
                if choice == '1':
                    return 'OPTION1'
                elif choice == '2':
                    return 'OPTION2'
                elif choice == '3':
                    return 'OPTION3'
        elif state == 'SUBMENU':
            choice = ''
            while not choice in ['1', '2', '3']:
                choice = input("Enter your choice: ")
                if choice == '1':
                    return 'OPTION1'
                elif choice == '2':
                    return 'OPTION2'
                elif choice == '3':
                    return 'MAIN_MENU'
        elif state in ['PLAY_WITH_CPU', 'PLAY_WITH_USER']:
            while True:
                print("You can go back by typing B")
                choice = input("Enter the point in x y format (For example 2 2 for center): ")
                if choice == 'B':
                    return 'MAIN_MENU'
                try :
                    i, j = map(
                        int,
                        choice.split(),
                    )
                    break
                except:
                    print("Invalid input. Try again")
                    continue

            i -= 1
            j -= 1

            return (i, j)
                
    def update(self):
        pass

    def exit(self):
        pass