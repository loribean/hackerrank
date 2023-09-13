function solveSudoku(sudoku) {
    rows = {};
    cols = {};
    boxes = {};
    toVisit = [];

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            let cell = sudoku[i][j];
            if (cell !== '.') {
                let box = Math.floor(i / 3) + '-' + Math.floor(j / 3);
                let row = rows[i] || Set();
                let col = cols[j] || Set();
                let currentBox = boxes[box] || Set();
                rows[i] = row.add(cell);
                cols[j] = col.add(cell);
                boxes[box] = currentBox.add(cell);
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

            if (rows[i].has(num) || cols[j].has(num) || boxes[box].has(num)) {
                continue;
            }

            rows[i] = rows[i].add(num);
            cols[j] = cols[j].add(num);
            boxes[box] = boxes[box].add(num);
            sudoku[i][j] = num;

            if (dfs()) {
                return true;
            } else {
                rows[i] = rows[i].delete(num);
                cols[j] = cols[j].delete(num);
                boxes[box] = boxes[box].delete(num);
                sudoku[i][j] = '.';
            }

        }

        return false;
    }

    dfs();
}