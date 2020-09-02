class Solution:
    def getSum(self, left, right):
        if left == 0:
            return self.Sum[right]
        else:
            return self.Sum[right] - self.Sum[left - 1]
        
    def dfs(self, left, right):
        if left == right:
            return 0
        if (left, right) in self.D:
            return self.D[(left, right)]
        res = 0
        for i in range(left, right):
            leftSum = self.getSum(left, i)
            rightSum = self.getSum(i + 1, right)
            if leftSum <= rightSum:
                res = max(res, leftSum + self.dfs(left, i))
            if leftSum >= rightSum:
                res = max(res, rightSum + self.dfs(i + 1, right))
        self.D[(left, right)] = res
        return res
        
    def stoneGameV(self, stoneValue: List[int]) -> int:
        self.Sum = [stoneValue[0]]
        for i in range(1, len(stoneValue)):
            self.Sum.append(stoneValue[i] + self.Sum[-1])
        self.D = dict()
        return self.dfs(0, len(stoneValue) - 1)
