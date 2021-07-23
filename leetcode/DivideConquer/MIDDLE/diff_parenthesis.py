# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results
        
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        for index, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])
                
                results.extend(compute(left, right, value))
        return results