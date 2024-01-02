class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def pre_order_with_queue(root):
    if not root:
        return
    
    queue = [root]

    while queue:
        current_node = queue.pop(0)
        print(current_node.key, end=' ')

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)