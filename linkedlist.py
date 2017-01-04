
class Node():
    def __init__(self, value, next_node=False, last_node=False):
        self.value = value
        self.nextNode = next_node
        self.lastNode = last_node
    def next(self):
        return self.nextNode
    def isLast(self):
        if not self.nextNode:
            return True
        return False
    def printValue(self):
        print(str(self.value)+' ', end='', flush=True)
        if self.nextNode:
            self.nextNode.printValue()
    def returnLast(self):
        if self.isLast():
            return self
        return self.nextNode.returnLast()
    def returnValue(self, string):
        if self.isLast():
            return string+'%s'%self.value
        return self.nextNode.returnValue(string+'%s '%self.value)
    def getLength(self, counter):
        if self.isLast:
            return counter
        return self.nextNode.getLength(counter+1)
    def last(self):
        return self.lastNode
    def getNextAfter(self, index):
        if index==0:
            return self
        return self.nextNode.getNextAfter(index-1)

class LinkedList():
    def __init__(self, firstNode):
        firstNode = Node(firstNode)
        self.firstNode = firstNode
    def addFirst(self, node):
        node = Node(node)
        self.firstNode.lastNode = node
        node.nextNode = self.firstNode
        self.firstNode = node
        self.printList()
    def append(self, node):
        node = Node(node)
        lastbefore = self.firstNode.returnLast()
        lastbefore.nextNode = node
        node.lastNode = lastbefore
        self.printList()
    def removeLast(self):
        self.firstNode.returnLast().lastNode.nextNode = None
        self.firstNode.returnLast().lastNode = None
        self.printList()
    def removeFirst(self):
        n = self.firstNode.next()
        self.firstNode.nextNode = None
        self.firstNode = n
        self.printList()
    def printList(self):
        self.firstNode.printValue()
    def returnList(self):
        self.firstNode.returnValue
    def look(self, index):
        return self.firstNode.getNextAfter(index).value
    def get_length(self):
        return self.firstNode.getLength(1)
    def sorted_insert(self, node):
        for index in range(0, self.get_length()):
            if self.look(index) > node:
                if index == 0:
                    self.addFirst(node)
                    return True
                self.insert(index, node)
                return True
        self.addLast(node)
        return False
    def insert(self, index, node):
        index = index - 1
        node = Node(node)
        target = self.firstNode.getNextAfter(index)
        after = target.nextNode
        node.lastNode = target
        node.nextNode = after
        target.nextNode = node
        after.lastNode = node
        self.printList()
