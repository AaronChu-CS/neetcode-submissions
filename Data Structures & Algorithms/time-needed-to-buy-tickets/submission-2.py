class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = tickets[k]
        x = 0
        for i in range(len(tickets)):
            if i <= k:
                x += min(tickets[i], t)
            else:
                x += min(tickets[i], t - 1) 
        return x