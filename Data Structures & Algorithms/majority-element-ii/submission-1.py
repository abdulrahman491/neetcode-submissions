class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hashSet = set(nums)
        hashMap = {}
        solutionList = []

        for key in hashSet:
            hashMap[key] = 0

        for num in nums:
            hashMap[num] += 1

        for key in hashMap:
            if hashMap[key] > len(nums) // 3:
                solutionList.append(key)

        return solutionList
