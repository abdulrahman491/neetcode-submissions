class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashSet = set(nums)
        hashMap = {}
        minFreq = None
        maxFreq = None

        for _ in hashSet:
            hashMap[_] = 0

        for _ in nums:
            hashMap[_] += 1

        minFreq = hashMap[nums[0]]
        maxFreq = minFreq

        for key in hashMap:
            if hashMap[key] > maxFreq:
                maxFreq = hashMap[key]
            elif hashMap[key] < minFreq:
                minFreq = hashMap[key]

        sIdx = 0
        eIdx = maxFreq - minFreq

        auxList = [[] for _ in range(eIdx + 1)]

        for key in hashMap:
            auxList[hashMap[key] - minFreq].append(key)

        j = eIdx
        res = []

        while j > -1 and k != 0:
            if auxList[j] != []:
                for key in auxList[j]:
                    res.append(key)
                    k -= 1
                    if k == 0:
                        break
                
            j -= 1

        return res
            



        
        
            