class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)
        
        if not root:
            return False
        if is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
