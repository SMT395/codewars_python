class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    
    def unwrap(node): return [getattr(node, attr) for attr in ['value', 'left', 'right']]

    if not node:
        return []
    else:
        output = unwrap(node)
        while Node in [type(node) for node in output]:    
            idx = [type(node) for node in output].index(Node)
            output.extend(unwrap(output[idx])[1:])
            output[idx] = unwrap(output[idx])[0]
        
        return [node for node in output if node]