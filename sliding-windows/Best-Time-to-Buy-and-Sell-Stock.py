class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_price=0
        for i in range(n):
            for j in range(i+1,n):
                if prices[i]<prices[j]:
                    price=prices[j]-prices[i]
                    max_price=max(max_price,price)
        return max_price