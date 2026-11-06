class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def capture(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != "O":
                return
            board[i][j] = "T"
            capture(i-1, j)
            capture(i+1, j)
            capture(i, j-1)
            capture(i, j+1)

        for i in range(m):
            for j in range(n):
                if (board[i][j] == "O" and (i in [0, m-1] or j in [0, n-1])):
                    capture(i, j)


        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"

        