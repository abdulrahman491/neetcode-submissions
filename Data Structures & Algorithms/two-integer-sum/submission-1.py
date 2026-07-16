class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashTable = set(nums)
        i = 0
        while i < len(nums) - 1:
            wanted = target - nums[i]
            if wanted in hashTable:
                j = i + 1
                while j < len(nums):
                    if nums[j] == wanted: 
                        return [i, j]
                    j += 1
            i += 1
                