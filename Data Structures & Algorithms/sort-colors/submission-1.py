class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 

        lIdx = 0
        rIdx = len(nums) - 1
        mIdx = 0


        while mIdx <= rIdx:

            if nums[mIdx] == 0:
                nums[mIdx], nums[lIdx] = nums[lIdx], nums[mIdx]
                lIdx += 1
            elif nums[mIdx] == 2:
                nums[mIdx], nums[rIdx] = nums[rIdx], nums[mIdx]
                rIdx -= 1
                mIdx -= 1

            mIdx += 1

        