# Add a new field to the Node class: `depth`. Depth's value is the max distance from the current node to any of the leaf
# in the current tree (or a subtree, if the current node is not a root node). E.g., any leaf node has a depth of 0.
# Update Node's __str__ and __repr__ implementation to print a node in the following form: "{<value>, <parent's value or
# None>, <depth>}"
# During the `add` operation make sure the `depth` is updated for all nodes it needs to be updated. Note that adding a
# node may or may not cause any node's `depth` to be changed at all. E.g. if you have a tree of two nodes: root
# (with value 100) and it's left child (with value 50), and you're adding a new node with value 150, then no `depth`
# will change. If in the same initial setup value 10 is added, then `depth` for both 50 and 100 will increase by 1.

class Node:
    def __init__(self, value, parent=None, depth=0):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.parent = parent
        self.depth = depth

    def __repr__(self):
        if self.parent:
            return '{%s, %s, %s}' %(self.value, self.parent.value, self.depth)
        else:
            return '{%s, %s, %s}' %(self.value, self.parent, self.depth)

    def __int__(self):
        return self.value

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, firstNode=None):
        if firstNode:
            self.firstNode = Node(firstNode, None, 0)
        else:
            self.firstNode = None

    def is_leaf(self, node):
        if node:
            return not bool(node.leftNode or node.rightNode)
        if node==None:
            return True

    def correct_depth(self, node):
        if not (node.rightNode and node.leftNode):
            return 0
        rd = 0
        if node.rightNode:
            rd = self.correct_depth(node.rightNode)
            node.rightNode.depth = rd
        ld = 0
        if node.leftNode:
            ld = self.correct_depth(node.leftNode)
            node.leftNode.depth = ld
        d = max([rd, ld]) + 1
        node.depth = d
        print(d)
        return d

    def get_depth(self, node):
        if not (node.rightNode and node.leftNode):
            return 0
        rd = 0
        if node.rightNode:
            rd = self.get_depth(node.rightNode)
        ld = 0
        if node.leftNode:
            ld = self.get_depth(node.leftNode)
        d = max([rd, ld])+1
        return d

    def add(self, value):
        cur = self.firstNode
        while not self.is_leaf(cur):
            if value > cur.value:
                if cur.rightNode:
                    cur = cur.rightNode
                    continue
                break
            elif value < cur.value:
                if cur.leftNode:
                    cur = cur.leftNode
                    continue
                break
        if value > cur.value:
            new = Node(value, cur, 0)
            cur.rightNode = new
        else:
            new = Node(value, cur, 0)
            cur.leftNode = new
        cur = new
        while cur.parent:
            cur.depth = self.get_depth(cur)
            cur = cur.parent
        cur.depth = self.get_depth(cur)


    def print_inorder(self):
        return self.recursive_printing()


    def recursive_printing(self, node=None, output=''):
        if not node:
            node=self.firstNode
        if node.leftNode:
            output = self.recursive_printing(node.leftNode, output)
        output += node.__repr__() + ' '
        if node.rightNode:
            output = self.recursive_printing(node.rightNode, output)
        return output.strip()

t = BST(100)
for x in [50, 150, 45, 55, 120, 170]:
    t.add(x)
print(t.print_inorder())