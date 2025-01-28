ifunction searchMatrix(matrix: number[][], target: number): boolean {
    let row: number[] = [];
    for (let i = 0; i < matrix.length; i++) {
        if (target < matrix[i][0]) {
            row = matrix[i - 1];
            while (row.length > 0) {
                const midIndex = Math.floor(row.length / 2); // Fix for finding the middle index
                const mid = row[midIndex];
                if (target < mid) {
                    row = row.slice(0, midIndex); // Correct slicing syntax
                } else if (target > mid) {
                    row = row.slice(midIndex + 1); // Correct slicing syntax
                } else if (target === mid) {
                    return true;
                }
            }
            return false;
        } else {
            continue;
        }
    }
    return false;
}

