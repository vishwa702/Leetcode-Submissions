from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,  j):
            q = deque([(i, j)])

            while q:
                (i, j) = q.pop()
                # print(f'\tPopping ({i}, {j})')

                visited.add((i, j))

                if i + 1 < m  and grid[i+1][j] == '1' and (i+1, j) not in visited:
                    q.append((i+1,  j))
                
                if i - 1 >= 0  and grid[i-1][j] == '1' and (i-1, j) not in visited:
                    q.append((i-1,  j))
                
                if j + 1 < n and grid[i][j+1] == '1' and (i, j+1) not in visited:
                    q.append((i, j+1))

                if j - 1 >= 0 and grid[i][j-1] == '1' and (i, j-1) not in visited:
                    q.append((i, j-1))

            del q


        # m rows, n columns
        m, n = len(grid), len(grid[0]) 

        visited = set()
        # print(f'\tVisited: {visited}')

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    # print(f'\nCalling BFS for ({i}, {j})')
                    bfs(i,  j)
                    # print(f'\tVisited: {visited}')
                    count += 1
                

        return count

