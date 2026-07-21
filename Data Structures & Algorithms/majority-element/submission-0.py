class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        keys = set(nums)
        hashMap = {}

        for elem in keys:
            hashMap[elem] = 0


        for _ in nums:
            hashMap[_] += 1

        
        for key in hashMap:
            if hashMap[key] >= len(nums) / 2:
                return key