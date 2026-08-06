class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[len(nums) - 1] >= nums[0]:
            return nums[0]

        
        left = 0 
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] >= nums[0]:
                left = middle + 1
            elif nums[middle] < nums[0]:
                if nums[middle] < nums[middle - 1]:
                    return nums[middle]
                right = middle - 1