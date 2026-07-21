class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if len(nums) == 0:
            return 0
            
        leftIdx = 0
        rightIdx = len(nums) - 1
        k = 0

        while leftIdx < rightIdx:
            if nums[leftIdx] == val:
                while rightIdx != leftIdx and nums[rightIdx] == val:
                    rightIdx -= 1
                nums[leftIdx] = nums[rightIdx]
                nums[rightIdx] = val
            leftIdx += 1

        i = 0
        while i < len(nums) and nums[i] != val:
            k += 1
            i += 1 

        return k