class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCount = 0

        for elem in nums:
            if elem == 0:
                zeroCount += 1


        if zeroCount > 1:
            for i in range(len(nums)):
                nums[i] = 0
        elif zeroCount == 1:
            for elem in nums:
                if elem != 0:
                    prod *= elem
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0
        elif zeroCount == 0:
            for elem in nums:
                prod *= elem
            for i in range(len(nums)):
                nums[i] = prod // nums[i]

        return nums