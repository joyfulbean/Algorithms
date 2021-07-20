# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dist = []
        for point in points:
            d1 = pow(point[0],2)
            d2 = pow(point[1],2)
            distance = sqrt(d1+d2)
            dist.append((distance,point))
            
        dist2 = []
        for i in sorted(dist):
            dist2.append(i[1])
            k -= 1
            if k == 0:
                break
        return dist2