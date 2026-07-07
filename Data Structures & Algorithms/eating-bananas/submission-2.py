class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max = piles[0]
        i = None
        for i in piles:
            if i > max:
                max = i

        if len(piles) == h:
            return max

        s = 1
        e = max
        k = None

        while s <= e:
            rate = (s + e) // 2
            hours = 0
            for i in piles:
                if i <= rate:
                    hours += 1
                elif i > rate and ((i % rate) != 0):
                    hours += (i // rate) + 1
                else:
                    hours += i / rate
            if hours <= h:
                k = rate
                e = rate - 1
            elif hours > h:
                s = rate + 1

        return k
