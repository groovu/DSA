class Solution:
    def gameStatus(board):
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                return board[i][0]
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return board[0][i]
        
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return board[0][2]
        return False
    
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0 for i in range(3)] for j in range(3)]
        player = "A"
        for move in moves:
            row = move[0]
            col = move[1]
            board[row][col] = player
            if player == "A":
                player = "B"
            else:
                player = "A"
        gameStatus = Solution.gameStatus(board)

        if len(moves) == 9 and not gameStatus:
            return "Draw"
        if len(moves) != 9 and not gameStatus:
            return "Pending"
        return gameStatus
        