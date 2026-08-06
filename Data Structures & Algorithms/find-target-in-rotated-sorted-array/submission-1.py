class Solution:
    def search(self, nums: List[int], target: int) -> int:
            

        left = 0
        right = len(nums) - 1
        targetPos = target < nums[0]  # True means right part, and false means left part
        middlePos = None

        while left <= right:
            middle = (left + right) // 2

            middlePos = nums[middle] < nums[0] #True means right part, and false means left part

            if middlePos == targetPos:
                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
            elif middlePos == True and targetPos == False:
                right = middle - 1
            elif middlePos == False and targetPos == True:
                left = middle + 1
        
        return -1
            

                

