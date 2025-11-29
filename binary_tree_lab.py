from typing import Optional


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


# Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Compute the maximum depth of a binary tree.

    Depth is defined as the number of nodes along the longest path
    from the root node down to the farthest leaf node.

    An empty tree has depth 0.
    """
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


# Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the lowest common ancestor (LCA) of nodes p and q in a Binary Search Tree.

    Uses the BST property:
      - If both p and q are less than current node, LCA is in the left subtree.
      - If both p and q are greater than current node, LCA is in the right subtree.
      - Otherwise, current node is the LCA (split point or equal to p/q).
    """
    current = root

    while current:
        # Both target nodes are in the left subtree
        if p.val < current.val and q.val < current.val:
            current = current.left
        # Both target nodes are in the right subtree
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            # Split point found
            return current

    return root
