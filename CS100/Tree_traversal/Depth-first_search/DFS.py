from Tree_node import TreeNode, sample_root_node, print_path, print_tree

## Sample tree structure
print_tree(sample_root_node)

## Depth-first-search function
def dfs(root, target, path=()):
    path = path + (root,)

    # Base Case
    if root.value == target:
        return path

    # Recursion
    for child in root.children:
        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found

    return None
        
path = dfs(sample_root_node, "F")
print(path)