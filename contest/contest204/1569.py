class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.chirdNum = 0
        self.res = 0
        
class Tree:
    def __init__(self, nums):
        self.root = TreeNode(nums[0])
        self.nums = nums
        
    def insert(self, n, node):
        if n > node.val:
            if node.right == None:
                node.right = TreeNode(n)
            else:
                self.insert(n, node.right)
        if n < node.val:
            if node.left == None:
                node.left = TreeNode(n)
            else:
                self.insert(n, node.left)
        
    def generate(self):
        for n in self.nums:
            self.insert(n, self.root)
            
    def child(self, node):
        if node == None:
            return 0
        node.chirdNum = 1 + self.child(node.left) + self.child(node.right)
        return node.chirdNum
    
    def comb(self, m, n):
        return self.frac(m) // (self.frac(n) * self.frac(m - n))
    
    def frac(self, n):
        res = 1
        for i in range(2, n + 1):
            res *= i
        return res
    
    def cal(self, node):
        if node == None:
            return 1
        leftNum = self.cal(node.left)
        rightNum = self.cal(node.right)
        leftChild = 0 if node.left == None else node.left.chirdNum
        rightChild = 0 if node.right == None else node.right.chirdNum        
        node.cal = leftNum * rightNum * self.comb(leftChild + rightChild, rightChild)        
        return node.cal       
        
            
        
class Solution:    
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        searchTree = Tree(nums)
        searchTree.generate()
        searchTree.child(searchTree.root)
        return (searchTree.cal(searchTree.root) - 1) % mod
