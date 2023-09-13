function solveSudoku(sudoku) {
    let rows = {};
    let cols = {};
    let boxes = {};
    let toVisit = [];

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            let cell = sudoku[i][j];
            if (cell !== '.') {
                let box = Math.floor(i / 3) + '-' + Math.floor(j / 3);
                rows[i] = rows[i] || new Set();
                cols[j] = cols[j] || new Set();
                boxes[box] = boxes[box] || new Set();

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

        let [i, j] = toVisit.pop();
        let box = Math.floor(i / 3) + '-' + Math.floor(j / 3);

        for (let num = 1; num <= 9; num++) {
            num = num.toString();
            if (rows[i].has(num) || cols[j].has(num) || boxes[box].has(num)) {
                continue;
            }

            rows[i].add(num);
            cols[j].add(num);
            boxes[box].add(num);
            sudoku[i][j] = num;

            if (dfs()) {
                return true;
            } else {
                rows[i].delete(num);
                cols[j].delete(num);
                boxes[box].delete(num);
                sudoku[i][j] = '.';
            }
        }

        toVisit.push([i, j]);
        return false;
    }

    if (dfs()) {
        return sudoku;
    } else {
        return "No solution exists!";
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