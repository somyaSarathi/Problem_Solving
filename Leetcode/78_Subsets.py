class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.allSubset = []
        self.arr = nums
        self.helper([])
        return self.allSubset
        
    def helper(self, sub: list[int], counter: int=0) -> None:
        if counter < len(self.arr):
            self.helper(sub, counter+1)
            self.helper(sub+[self.arr[counter]], counter+1)
            return None
        else:
            self.allSubset.append(sub)
