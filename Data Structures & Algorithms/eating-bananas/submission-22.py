class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        l_hours = self.evaluate_pile(l, piles)
        r_hours = self.evaluate_pile(r, piles)
        min_pph = l
        count = 0

        while l <= r:
            count += 1
            m = (r + l) // 2
            print(f"l {l} | m {m} | r {r}")
            m_hours = self.evaluate_pile(m, piles)
            print(f"{l_hours} {r_hours} {m_hours}")
            if m_hours > h:
                print("here")
                l = m + 1
                l_horus = self.evaluate_pile(l, piles)
            elif m_hours <= h:
                print("HERE")
                min_pph = m
                r = m - 1
                r_hours = self.evaluate_pile(r, piles)
        
        return min_pph

    
    def evaluate_pile(self, pile_per_hour: int, piles: List[int]) -> int:
        hours = 0
        if pile_per_hour <= 0:
            return 0
        
        for pile in piles:
            hours += math.ceil(pile / pile_per_hour)
        
        return hours
            