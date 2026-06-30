class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0 
        lastIdx = len(nums) - 1
        while i != lastIdx:
            j = i + 1
            while j != lastIdx + 1:
                if nums[i] == nums[j]:
                    return nums[i]
                j = j + 1
            i = i + 1