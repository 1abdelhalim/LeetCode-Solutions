# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        if not root:
            return ""

        queue = deque([root])
        result = []
        
        while queue:
            curr = queue.popleft()
            if curr:
                result.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])

        i = 1 
        while queue:
            curr = queue.popleft()

            if nodes[i] != "null":
                curr.left = TreeNode(int(nodes[i]))
                queue.append(curr.left)
            i += 1 

            if nodes[i] != "null":
                curr.right = TreeNode(int(nodes[i]))
                queue.append(curr.right)
            i += 1 

        return root 
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans