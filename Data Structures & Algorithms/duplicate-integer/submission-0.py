class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set(nums)
        if len(uniqueSet) < len(nums):
            return True

        return False