class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        posCount = 0
        minNum = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                posCount += 1
            elif nums[i] < 0:
                nums[i] = 0

        maxNum = posCount + 1

        for i in range(len(nums)):
            if abs(nums[i]) < posCount + 1 and abs(nums[i]) > 0:
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1
                elif nums[abs(nums[i]) - 1] == 0:
                    nums[abs(nums[i]) - 1] = -posCount - 1

        i = minNum
        while i < maxNum:
            if nums[i - 1] > 0:
                return i
            i += 1

        return posCount + 1


        