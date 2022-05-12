class Solution:
    def isPath(self, grid: list[list[int]], r: int, c: int) -> bool:
        try: return not grid[r][c]
        except IndexError: return False
        
    
    def uniquePathsWithObstacles(self, grid: List[List[int]], r: int=0, c: int=0, memo: dict=None) -> int:
        if memo is None: memo = dict()
        if (r, c) in memo: return memo[(r, c)]

        # base case
        if len(grid) == 0: return 0
        if grid[r][c] == 1: return 0
        if r == len(grid)-1 and c == len(grid[0])-1: return 1

        memo[(r, c)] = 0
        if r+1 < len(grid) and self.isPath(grid, r+1, c):
            memo[(r, c)] += self.uniquePathsWithObstacles(grid, r+1, c, memo)
        if c+1 < len(grid[0]) and self.isPath(grid, r, c+1):
            memo[(r, c)] += self.uniquePathsWithObstacles(grid, r, c+1, memo)

        return memo[(r, c)]
