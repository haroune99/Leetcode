function searchMatrix(matrix: number[][], target: number): boolean {
    let row: number[] = [];
    for (let i = 0; i < matrix.length; i++) {
        if (target < matrix[i][0]) {
            if (i - 1 < 0) {
                return false; // If `i - 1` is out of bounds, target is not in the matrix
            }
            row = matrix[i - 1];
            while (row.length > 0) {
                const midIndex = Math.floor(row.length / 2); // Calculate the middle index
                const mid = row[midIndex];
                if (target < mid) {
                    row = row.slice(0, midIndex); // Slice left half
                } else if (target > mid) {
                    row = row.slice(midIndex + 1); // Slice right half
                } else {
                    return true; // Target found
                }
            }
            return false; // Target not found in the row
        }
    }

    // If the loop completes and the target is greater than all row start values
    row = matrix[matrix.length - 1];
    while (row.length > 0) {
        const midIndex = Math.floor(row.length / 2); // Calculate the middle index
        const mid = row[midIndex];
        if (target < mid) {
            row = row.slice(0, midIndex); // Slice left half
        } else if (target > mid) {
            row = row.slice(midIndex + 1); // Slice right half
        } else {
            return true; // Target found
        }
    }

    return false; // Target not found
}

