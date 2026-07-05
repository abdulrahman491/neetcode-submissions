class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        s = 0 
        e = len(nums) - 1

        if target > nums[e]:
            return e + 1
        elif target < nums[s]:
            return 0
        
        while s <= e:
            m = (s + e) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                e = m - 1
            elif target > nums[m]:
                s = m + 1
        else:
            return s
