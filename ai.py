import random

class AI:
    def __init__(self) -> None:
        pass
    
    def move(self, board, flag):

        # Place at the center if available
        if board[1][1] == 0:
            return 1, 1

        opportunities = []
        for k in range(3):
            # X X -
            if board[k][0] == board[k][1] and board[k][0] != 0 and board[k][2] == 0:
                opportunities.append((k, 2, board[k][0]))
            # - X X
            if board[k][1] == board[k][2] and board[k][1] != 0 and board[k][0] == 0:
                opportunities.append((k, 0, board[k][2]))
            # X - X
            if board[k][0] == board[k][2] and board[k][2] != 0 and board[k][1] == 0:
                opportunities.append((k, 1, board[k][0]))

            # X - -
            # X - -
            # - - -
            if board[0][k] == board[1][k] and board[0][k] != 0 and board[2][k] == 0:
                opportunities.append((2, k, board[0][k]))
            # - - -
            # X - -
            # X - -
            if board[1][k] == board[2][k] and board[1][k] != 0 and board[0][k] == 0:
                opportunities.append((0, k, board[1][k]))
            # X - -
            # - - -
            # X - -
            if board[0][k] == board[2][k] and board[0][k] != 0 and board[1][k] == 0:
                opportunities.append((1, k, board[0][k]))

        # X - -
        # - X -
        # - - -
        if board[0][0] == board[1][1] and board[0][0] != 0 and board[2][2] == 0:
            opportunities.append((2, 2, board[1][1]))
        # - - -
        # - X -
        # - - X
        if board[1][1] == board[2][2] and board[1][1] != 0 and board[0][0] == 0:
            opportunities.append((0, 0, board[2][2]))
        # X - -
        # - - -
        # - - X
        if board[0][0] == board[2][2] and board[0][0] != 0 and board[1][1] == 0:
            opportunities.append((1, 1, board[0][0]))

        # - - X
        # - X -
        # - - -
        if board[0][2] == board[1][1] and board[0][2] != 0 and board[2][0] == 0:
            opportunities.append((2, 0, board[0][2]))
        # - - -
        # - X -
        # X - -
        if board[1][1] == board[2][0] and board[1][1] != 0 and board[0][2] == 0:
            opportunities.append((0, 2, board[2][0]))
        # - - X
        # - - -
        # X - -
        if board[0][2] == board[2][0] and board[0][2] != 0 and board[1][1] == 0:
            opportunities.append((1, 1, board[0][2]))

        # Generate random i and j if there is no opportunities
        if len(opportunities) == 0:
            i = random.randrange(0, 3)
            j = random.randrange(0, 3)
        else:
            for opp in opportunities:
                if opp[2] == flag:
                    return opp[0], opp[1]
            random_chosen = opportunities[random.randrange(len(opportunities))]
            return random_chosen[0], random_chosen[1]
        # Generate random i and j's while there are occupied i and j's
        while board[i][j] != 0:
            i = random.randrange(0, 3)
            j = random.randrange(0, 3)
        return i, j