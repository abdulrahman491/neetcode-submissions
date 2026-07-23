class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # First check - Rows Only

        for i in range(9):
            dupCheck = [False for _ in range(9)]
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if dupCheck[num - 1] == False:
                        dupCheck[num - 1] = True
                    else:
                        return False

        # Second check - Columns Only
        for i in range(9):
            dupCheck = [False for _ in range(9)]
            for j in range(9):
                if board[j][i] != ".":
                    num = int(board[j][i])
                    if dupCheck[num - 1] == False:
                        dupCheck[num - 1] = True
                    else:
                        return False

        # Third check - 9 Square sub-boxes

        for k in range(9):
            dupCheck = [False for _ in range(9)]
            if k == 0 or k == 1 or k == 2:
                iRange = 0
            elif k == 3 or k == 4 or k == 5:
                iRange = 3
            elif k == 6 or k == 7 or k == 8:
                iRange = 6

            if k == 0 or k == 3 or k == 6:
                jRange = 0
            elif k == 1 or k == 4 or k == 7:
                jRange == 3
            elif k == 2 or k == 5 or k == 8:
                jRange = 6

            for i in range(iRange, iRange + 3):
                for j in range(jRange, jRange + 3):
                    if board[i][j] != ".":
                        num = int(board[i][j])
                        if dupCheck[num - 1] == False:
                            dupCheck[num - 1] = True
                        else:
                            return False

        return True
