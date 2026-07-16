class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for num in nums:
            hashMap[num] = 0

        for num in nums:
            hashMap[num] += 1

        
        i = 0
        while i < len(nums) - 1:
            wanted = target - nums[i]
                
            if wanted in hashMap:
                if wanted != nums[i]:
                    j = i + 1
                    while j < len(nums):
                        if nums[j] == wanted: 
                            return [i, j]
                        j += 1
                elif wanted == nums[i]:
                    if hashMap[wanted] > 1:
                        j = i + 1
                        while j < len(nums):
                            if nums[j] == wanted: 
                                return [i, j]
                            j += 1

            i += 1
                