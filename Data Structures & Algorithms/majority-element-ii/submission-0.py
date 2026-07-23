class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hashSet = set(nums)
        hashMap = {}
        solutionList = []

        for _ in hashSet:
            hashMap[_] = 0

        for _ in nums:
            hashMap[_] += 1

        for _ in hashMap:
            if hashMap[_] > len(nums) // 3:
                solutionList.append(_)

        return solutionList