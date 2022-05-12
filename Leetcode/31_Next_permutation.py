class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1
        if i>=0:
            j = len(nums)-1
            while(nums[j]<=nums[i]):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i+1)
        
    
    def reverse(self, nums: list[int], start: int=0):
        j = len(nums)-1
        while(start < j):
            nums[start], nums[j] = nums[j], nums[start]
            start += 1
            j -= 1
