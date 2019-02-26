# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def func(root):
            if root==None:
                return 0,None
            if root.left==None and root.right==None:
                return 1,root.val
            numleft,valleft = func(root.left)
            numright,valright=func(root.right)
            if (valleft==None or valleft==root.val) and (valright==None or valright==root.val):
                return numleft+numright+1,root.val
            return numleft+numright,'noway'
        return func(root)[0]