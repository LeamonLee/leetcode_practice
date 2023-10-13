'''
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Example 1:
Input: root = [2,1,3]
Output: [2,1,3]

Example 2:
Input: root = []
Output: []
'''
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
        res=""
        def preorder(node):
            nonlocal res
            if node:
                if res=="":
                    res+=f"{node.val}"
                else:
                    res+=f" {node.val}"
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        # print(f"res:{res}")
        return res

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data: return None

        def build(minNum, maxNum, q):
            if not q: return None
            # print(f"q[0]:{q[0]}, minNum:{minNum}, maxNum:{maxNum}, q:{q}")
            if minNum < q[0] < maxNum:
                val = q.popleft()
                node = TreeNode(val)
                node.left = build(minNum, node.val, q)
                node.right = build(node.val, maxNum, q)
                return node

        q = deque(int(num) for num in data.split(" "))
        # print(f"q:{q}")
        root = build(float("-inf"), float("inf"), q)
        return root