class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)
        cnt = [] 
        start = -1
        minus = []
        for i in range(len(nums)):
            if nums[i] != 0 and start < 0:
                start = i
                minus = []
            if nums[i] == 0 and start >= 0:
                end = i - 1                
                cnt.append((start, end, minus))
                start = -1
            if nums[i] < 0:
                minus.append(i)
        res = 0
        for start, end, minus in cnt:
            if len(minus) % 2 == 0:
                res = max(res, end + 1 - start)
            else:
                res = max(res, end - minus[0], minus[-1] - start)
        return res
