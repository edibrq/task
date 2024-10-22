class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteLeaves(root, target):
    if not root:
        return None

    stack = [(root, None, None)]  # (node, parent, is_left_child)
    to_delete = []

    while stack:
        node, parent, is_left_child = stack.pop()

        if node.left:
            stack.append((node.left, node, True))
        if node.right:
            stack.append((node.right, node, False))

        if not node.left and not node.right and node.val == target:
            to_delete.append((parent, is_left_child))

    for parent, is_left_child in to_delete:
        if parent:
            if is_left_child:
                parent.left = None
            else:
                parent.right = None
        else:
            root = None

    return root