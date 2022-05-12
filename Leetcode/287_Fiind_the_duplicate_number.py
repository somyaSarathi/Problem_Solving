class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        numSet = set()
        for num in nums:
            if num in numSet:
                return num
            numSet.add(num)
