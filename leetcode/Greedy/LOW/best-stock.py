# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(prices)-1):
            #값이 오르는경우 매범 그리디 계산
            if prices[i] < prices[i+1]:
                result += prices[i+1] - prices[i] 
        return result
                
#0보다 크면 무조건 이익이 있는거니까 취하는 방식
# return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))