class Solution:
    def climbStairs(self, steps: int) -> int:
        if steps == 0: return 0
        if steps == 1: return 1
        if steps == 2: return 2

        memo = [0, 1, 2] + [0]*(steps-2)
        for i in range(3, steps+1):
            memo[i] = memo[i-2] + memo[i-1]
        
        return memo[steps]
