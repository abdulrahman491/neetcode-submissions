class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        
        seq = 2
        gap = len(nums) // seq

        while gap > 0: 

            fIdx = gap

            while fIdx < len(nums):
                tempIdx = fIdx
                bIdx = tempIdx - gap

                while bIdx >= 0 and nums[tempIdx] < nums[bIdx]:
                    nums[tempIdx], nums[bIdx] = nums[bIdx], nums[tempIdx]
                    bIdx -= gap
                    tempIdx -= gap

                fIdx += 1

            seq *= 2
            gap = len(nums) // seq


        