# https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #모든 주유소 방문 가능 여부
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            #출발점이 안 되는 지점 판별:
            #어 안되는 애가 생겼네, 불가능 초기화 움직여!! 
            if gas[i] + fuel < cost[i]:
                start = i+1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start