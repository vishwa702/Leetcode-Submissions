import numpy as np
from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid = np.array(grid)

        d = dict()
        col_counts = defaultdict(int)

        for col in grid.T:
            col = tuple(col)
            d[col] = 0
            col_counts[col] += 1

        # print(f'd:\n{d}' )

        for row in grid: 
            row = tuple(row)
            # print(f'processing row: {row}')
            if row in d:
                # print(f'adding count for row: {row} ')
                d[row] += col_counts[row]
        
        print(f'd:\n{d}' )
        return sum(d.values())
