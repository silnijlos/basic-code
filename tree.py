class Node():
    def __init__(self, value, parent=None):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.parent = parent

    def __repr__(self):
        return self.value
    def __int__(self):
        return self.value
    def __str__(self):
        return str(self.value)

    def recursive_printing(self, output=''):
        if self.leftNode:
            output = self.leftNode.recursive_printing(output)
        output += str(self.value)+' '
        if self.rightNode:
            output = self.rightNode.recursive_printing(output)
        return output


class BST():
    def __init__(self, firstNode=None):
        if firstNode:
            self.firstNode = Node(firstNode)
        else:
            self.firstNode = None

    def is_last(self, node):
        return not bool(node.leftNode or node.rightNode)

    def add(self, value):
        cur = self.firstNode
        while not self.is_last(cur):
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
            new = Node(value, cur)
            cur.rightNode = new
        else:
            new = Node(value, cur)
            cur.leftNode = new

    def print_inorder(self):
        return self.firstNode.recursive_printing()
t = BST(100)
t.add(50)
t.add(200)
t.add(10)
print(t.print_inorder())