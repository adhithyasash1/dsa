# https://leetcode.com/problems/path-sum/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False

        if root.val == targetSum and root.left == None and root.right == None:
            return True

        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)


# https://leetcode.com/problems/path-sum-ii/submissions/
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        self.findPaths(root, targetSum, [], result)
        return result

    def findPaths(self, node, targetSum, current, result):
        if node == None:
            return

        current.append(node.val)

        if node.val == targetSum and node.left == None and node.right == None:
            result.append(list(current))
        else:
            self.findPaths(node.left, targetSum-node.val, current, result)
            self.findPaths(node.right, targetSum-node.val, current, result)

        # backtracking
        del current[-1]

# https://leetcode.com/problems/sum-root-to-leaf-numbers/
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.findSum(root, 0)

    def findSum(self, node, ps):
        if node == None:
            return 0

        cs = ps * 10 + node.val

        # leaf node check
        if node.left == None and node.right == None:
            return cs

        return self.findSum(node.left, cs) + self.findSum(node.right, cs)


# https://leetcode.com/problems/diameter-of-binary-tree/
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dia = 0
        self.diameter(root)
        return self.dia-1

    def diameter(self, root):
        if root == None:
            return 0

        leftHeight = self.diameter(root.left)
        rightHeight = self.diameter(root.right)

        if leftHeight is not None and rightHeight is not None:
            diaForCurrentNode = leftHeight + rightHeight + 1

            # update the global one
            self.dia = max(self.dia, diaForCurrentNode)

        return max(leftHeight, rightHeight) + 1
