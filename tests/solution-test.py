from src.solution import TreeNode, deleteLeaves


def test_deleteLeaves():
    def build_tree_from_list(lst):
        if not lst:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in lst]
        for index in range(len(nodes)):
            if nodes[index] is not None:
                left_index = 2 * index + 1
                right_index = 2 * index + 2
                if left_index < len(nodes):
                    nodes[index].left = nodes[left_index]
                if right_index < len(nodes):
                    nodes[index].right = nodes[right_index]
        return nodes[0]

    def tree_to_list(root):
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    # Test Case 1: Single Node Tree
    root = build_tree_from_list([1])
    target = 1
    expected = []
    result = tree_to_list(deleteLeaves(root, target))
    assert result == expected, f"Test Case 1 Failed: Expected {expected}, got {result}"

    # Test Case 2: No Target Leaves
    root = build_tree_from_list([1, 2, 3])
    target = 4
    expected = [1, 2, 3]
    result = tree_to_list(deleteLeaves(root, target))
    assert result == expected, f"Test Case 2 Failed: Expected {expected}, got {result}"

    # Test Case 3: All Leaves Are Targets
    root = build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    target = 4
    expected = [1, 2, 3, None, 5, 6, 7]
    result = tree_to_list(deleteLeaves(root, target))
    assert result == expected, f"Test Case 3 Failed: Expected {expected}, got {result}"

    # Test Case 4: Mixed Leaves
    root = build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    target = 5
    expected = [1, 2, 3, 4, None, 6, 7]
    result = tree_to_list(deleteLeaves(root, target))
    assert result == expected, f"Test Case 4 Failed: Expected {expected}, got {result}"

    # Test Case 5: Nested Target Leaves
    root = build_tree_from_list([1, 2, 3, 2, None, 2, 4])
    target = 2
    expected = [1, None, 3, None, 4]
    result = tree_to_list(deleteLeaves(root, target))
    assert result == expected, f"Test Case 5 Failed: Expected {expected}, got {result}"

    print("All test cases passed!")

# Run the tests
test_deleteLeaves()
