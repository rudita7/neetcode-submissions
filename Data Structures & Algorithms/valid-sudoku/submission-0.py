class Solution:
    def isValidSudoku(self, board):
        
        for row in board:
            seen = set()
            for num in row:
                if num in seen and num != ".":
                    return False
                else:
                    seen.add(num)

    
        for j in range(0,9,1):  #column
            seen_column = set()
            for i in range(0,9,1):  #row
                if board[i][j]  in seen_column and board[i][j] != ".":
                    return False
                else:
                    seen_column.add(board[i][j])
                

        for i in range(0,9,3):
            for j in range(0,9,3):
                seen_all = set()
                for r in range(0,3,1):
                    for c in range(0,3,1):
                        if board[i+r][j+c] in seen_all and board[i+r][j+c] != ".":
                            return False
                        else:
                            seen_all.add(board[i+r][j+c])
        return True