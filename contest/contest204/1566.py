class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        string = ""
        for n in arr:
            string += chr(n)
        for i in range(len(arr)):  
            flag = True
            for j in range(1, k):
                if i + (j + 1) * m > len(arr):
                    flag = False
                    break
                if string[i + j * m: i + (j + 1) * m] != string[i: i + m]:
                    flag = False
                    break
            if flag:
                return True            
        return False
