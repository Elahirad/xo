from abc import abstractmethod, ABC

from interfaces.pygame_interface.constants import HEIGHT, WIDTH, SQUARE_SIZE

class BoardManagerInterface(ABC):
    @abstractmethod
    def clear_board(self):
        pass

    @abstractmethod
    def clear_scores(self):
        pass
    
    @property
    @abstractmethod
    def board(self):
        pass
    @board.setter
    @abstractmethod
    def board(self, value):
        pass

    @property
    @abstractmethod
    def x_wins(self):
        pass

    @x_wins.setter
    @abstractmethod
    def x_wins(self, value):
        pass
    
    @property
    @abstractmethod
    def o_wins(self):
        pass

    @o_wins.setter
    @abstractmethod
    def o_wins(self, value):
        pass

class BoardManager(BoardManagerInterface):
    def __init__(self) -> None:
        self.__board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__x_wins = 0
        self.__o_wins = 0
    
    def clear_board(self):
        self.__board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    def clear_scores(self):
        self.__x_wins = 0
        self.__o_wins = 0

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, value):
        for row in value:
            for el in row:
                if el not in [0, 1, 2]:
                    raise ValueError("Only (0, 1, 2) values are accpeted.")
        self.__board = value

    @property
    def x_wins(self):
        return self.__x_wins

    @x_wins.setter
    def x_wins(self, value):
        if value < 0:
                raise ValueError("Only zero or positive values allowed.")
        self.__x_wins = value
    
    @property
    def o_wins(self):
        return self.__o_wins

    @o_wins.setter
    def o_wins(self, value):
        if value < 0:
                raise ValueError("Only zero or positive values allowed.")
        self.__o_wins = value

class GameManagerInterface(ABC):
    @abstractmethod
    def check_win(self, board):
        pass
    @abstractmethod
    def is_ended(self, board):
        pass

class GameManager(GameManagerInterface):
    def __init__(self) -> None:
        pass
    
    def check_win(self, board) -> tuple[bool, int]:
        for i in range(3):
            # X X X <- check for this winning situation
            if (
                board[i][0] == board[i][1]
                and board[i][1] == board[i][2]
                and board[i][0] != 0
            ):
                return True, board[i][1]
            # X
            # X <- check for this winning situation
            # X
            if (
                board[0][i] == board[1][i]
                and board[1][i] == board[2][i]
                and board[0][i] != 0
            ):
                return True, board[0][i]
        # X - -
        # - X - <- check for this winning situation
        # - - X
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
            return True, board[0][0]
        # - - X
        # - X - <- check for this winning situation
        # X - -
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:
            return True, board[0][2]
        return False, None
    
    def is_ended(self, board) -> bool:  # Check if the game is ended
        count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    count += 1
        if count == 0:
            return True
        return False