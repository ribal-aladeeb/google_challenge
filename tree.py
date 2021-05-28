def build_tree(h):
    num_nodes = sum([2 ** (x) for x in range(h)])
    tree = [0 for _ in range(num_nodes)]

    def post_order(array, idx=0, visited=0):
        """Fill the tree values in post_order"""
        if idx >= len(array):
            return visited
        leftchild = idx * 2 + 1
        rightchild = idx * 2 + 2
        v = post_order(array, leftchild, visited=visited)
        v = post_order(array, rightchild, visited=v)
        latest = v + 1
        array[idx] = latest
        return latest

    post_order(tree)

    return tree


def solution(h, q):
    tree = build_tree(h)
    p = []
    for child in q:
        child_idx = tree.index(child)
        if child_idx == 0:  # root node has no parent
            p.append(-1)
        
        else:
            parent_idx = (child_idx - 1) // 2
            p.append(tree[parent_idx])
    return p


