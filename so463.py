from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        width = len(grid[0])
        hight = len(grid)
        island = []
        res = 0
        for i in range(hight):
            for j in range(width):
                if grid[i][j] == 1:
                    island.append((i, j))
        print(island)
        for pos in island:
            if pos[0] == 0 or grid[pos[0] - 1][pos[1]] == 0:
                res += 1
            if pos[0] == hight - 1 or grid[pos[0] + 1][pos[1]] == 0:
                res += 1
            if pos[1] == 0 or grid[pos[0]][pos[1] - 1] == 0:
                res += 1
            if pos[1] == width-1 or grid[pos[0]][pos[1] + 1] == 0:
                res += 1
        return res
