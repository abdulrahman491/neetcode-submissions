class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left = 0 
        right = len(nums) - 1
        while left <= right and nums[left] == nums[right]:
            if nums[left] == target:
                return True
            left += 1
        idx0 = left
        
        if left <= right:
            targetPos = target < nums[idx0] #True is right

        while left <= right:

            middle = (left + right) // 2
            middlePos = nums[middle] < nums[idx0] #True is right

            if targetPos == middlePos:
                if target == nums[middle]:
                    return True
                elif target < nums[middle]:
                    right = middle - 1
                elif target > nums[middle]:
                    left = middle + 1
            elif targetPos == False and middlePos == True:
                right = middle - 1
            elif targetPos == True and middlePos == False:
                left = middle + 1

        return False