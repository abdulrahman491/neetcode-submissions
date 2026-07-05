class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1

        if target > nums[end] or target < nums[start]:
            return -1

        while start <= end: 
            m = (start + end) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                end = m - 1
            else:
                start = m + 1
        else: 
            return -1