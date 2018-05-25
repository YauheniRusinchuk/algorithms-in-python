class Node:

    def __init__(self,data):
        self.data = data
        self.nextNode = None

    def remove(self,data,previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data,self)


class LinkedList:

    def __init__(self):
        self.head = None
        self.counter = 0


    #O(N)
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode

    #O(1)
    def insert(self,data):

        self.counter += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size(self):
        return self.counter

    #O(N)
    def insertEnd(self,data):

        if self.head is None:
            self.insert(data)
            return

        self.counter += 1

        newNode = Node(data)
        actualNode = self.head


        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode


    #O(N)
    def remove(self,data):

        self.counter -= 1

        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data,self.head)



linkedlist = LinkedList()

linkedlist.insert(12)
linkedlist.insert(23)
linkedlist.insert(44)
linkedlist.insertEnd(55)


linkedlist.traverseList()
