# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

 

# Example 1:


# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:


 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.


from collections import deque, defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        #use dfs to solve the sudoku
        #use backtracking to solve the sudoku
        rows,cols,boxes,to_visit =  defaultdict(set), defaultdict(set), defaultdict(set), deque()

        # we need loop through the whole board to get the initial state
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.': #if not empty, add to rows, cols, boxes
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3,j//3)].add(board[i][j])
                else:
                    to_visit.append((i,j)) # if empty, add to to_visit

        def dfs():
            if not to_visit: #if to_visit is empty, we have solved the sudoku!!
                return True
            i,j = to_visit[0] #get the first empty cell
            box = (i//3,j//3) #get the box number

            for num in {'1','2','3','4','5','6','7','8','9'}: #try each number
                if num not in rows[i] and num not in cols[j] and num not in boxes[box]: #if the number is not in the row, col, box, we can add it to the board
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)
                    board[i][j] = num
                    to_visit.popleft() #remove the cell from to_visit since we have TRIED it
                    if dfs(): #if dfs returns True, we have solved the sudoku
                        return True
                    else: #if dfs returns False, we need to backtrack and try another number
                        rows[i].remove(num)
                        cols[j].remove(num)
                        boxes[box].remove(num)
                        board[i][j] = '.'
                        to_visit.appendleft((i,j))

            return False #if we have tried all numbers and none of them works, we return False
        
        dfs()



        