function solveSudoku(sudoku) {
    const rows = {};
    const cols = {};
    const boxes = {};
    const toVisit = [];
  
    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        const cell = sudoku[i][j];
        if (cell !== ".") {
          const box = Math.floor(i / 3) + "-" + Math.floor(j / 3);
          rows[i] = rows[i]  || new Set();
          cols[j] = cols[j] || new Set();
          boxes[box] = boxes[box] ||  new Set();
  
          rows[i].add(cell);
          cols[j].add(cell);
          boxes[box].add(cell);
        } else {
          toVisit.push([i, j]);
        }
      }
    }
  
    function dfs() {
      if (toVisit.length === 0) {
        return true;
      }
  
      const [i, j] = toVisit.pop() ?? [0, 0];
      const box = Math.floor(i / 3) + "-" + Math.floor(j / 3);
  
      for (let num = 1; num <= 9; num++) {
        const numStr = num.toString();
        if (
          rows[i].has(numStr) ||
          cols[j].has(numStr) ||
          boxes[box].has(numStr)
        ) {
          continue;
        }
  
        rows[i].add(numStr);
        cols[j].add(numStr);
        boxes[box].add(numStr);
        sudoku[i][j] = numStr;
  
        if (dfs()) {
          return true;
        } else {
          rows[i].delete(numStr);
          cols[j].delete(numStr);
          boxes[box].delete(numStr);
          sudoku[i][j] = ".";
        }
      }
  
      toVisit.push([i, j]);
      return false;
    }
  
    if (dfs()) {
      return sudoku;
    } else {
      return undefined;
    }
  }

  const solvedSudoku = solveSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]);

console.log(solvedSudoku);