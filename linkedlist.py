
class Node():
    def __init__(self, value, next_node=False, prev_node=False):
        self.value = value
        self.nextNode = next_node
        self.prevNode = prev_node

    def next(self):
        return self.nextNode

    def isLast(self):
        if not self.nextNode:
            return True
        return False


    def isFirst(self):
        if not self.prevNode:
            return True
        return False

    def prev(self):
        return self.prevNode
    
    def __repr__(self):
        return str(self.value)

class LinkedList():
    def __init__(self, firstNode):
        firstNode = Node(firstNode)
        self.firstNode = firstNode

    def addFirst(self, value):
        node = Node(value)
        self.firstNode.lastNode = node
        node.nextNode = self.firstNode
        self.firstNode = node

    def append(self, value):
        node = Node(value)
        last = self.look(self.getLength()-1)
        last.nextNode = node
        node.prevNode = last

    def removeLast(self):
        last = self.look(self.getLength()-1)
        beforelast = self.look(self.getLength()-2)
        beforelast.nextNode = None
        last.prevNode = None

    def removeFirst(self):
        n = self.firstNode.next()
        self.firstNode.nextNode = None
        self.firstNode = n
    
    def __repr__(self):
        s = ''
        cur = self.firstNode
        s += str(cur.value)+' '
        while not cur.isLast():
            cur = cur.nextNode
            s += str(cur.value)+' '
        return s.strip()


    def look(self, index):
        cur = self.firstNode
        i = 0
        while index > i:
            cur = cur.nextNode
            i += 1
        return cur

    def getLength(self):
        cur = self.firstNode
        i = 1
        while not cur.isLast():
            i += 1
            cur = cur.nextNode
        return i

    def sortedInsert(self, value):
        cur = self.firstNode
        if cur.value > value:
            self.addFirst(value)
            return True
        index = 0
        while not cur.isLast() and cur.value < value:
            index += 1
            cur = cur.nextNode
        print(index)
        self.insert(index, value)


    def insert(self, index, value):
        index = index - 1
        node = Node(value)
        target = self.look(index)
        after = target.nextNode
        node.lastNode = target
        node.nextNode = after
        target.nextNode = node
        after.lastNode = node
