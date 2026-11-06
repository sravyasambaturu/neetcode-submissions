class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])

        def dfs(r, c, i):
            #base case if we found the word
            if i == len(word):
                return True

            #if its overbounds or wrong character
            if (r < 0 or c < 0 or r >= rows or c >= columns or board[r][c] != word[i]):
                return False

            #backtracking step 
            #save the original as visited and mark it #
            temp = board[r][c]
            board[r][c] = "#"

            #check all 4 directions if any of the path returns true the whole thing is true
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            #backtracking step
            #restore so that other paths can be used
            board[r][c] = temp

            return found

        #we must try for every cell on board
        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True

        return False

