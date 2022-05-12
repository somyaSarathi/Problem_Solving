class Solution:
    def uniquePaths(self, m: int, n: int, memo: dict=None) -> int:
        if memo is None: memo = {}
        if (m, n) in memo: return memo[(m, n)]

        # base case
        if n == 0 or m == 0: return 0
        if n == 1 or m == 1: return 1

        memo[(m, n)] = 0
        memo[(m, n)] += self.uniquePaths(m-1, n, memo)
        memo[(m, n)] += self.uniquePaths(m, n-1, memo)

        return memo[(m, n)]
