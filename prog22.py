class Node:
    def __init__(self, data):
        self.data = data
        self.next : Node = None

    def print(self):
        print(self.data)


class Node2:
    def __init__(self, data):
        self.data = data
        self.prev: Node = None
        self.next: Node = None

    def print(self):
        print(self.data)

#Single-linked list
class LList:
    def __init__(self):
        self.first : Node = None
        self.last: Node = None

    def push (self, data):
        #Create new node
        n = Node(data)

        #list is empty
        if self.first == None:
            self.first = n
            self.last = n

        #Connect behind the last node
        else:
            self.last.next = n
            self.last = n

    def print(self):
        print('List:')
        #Get first node
        n = self.first

        #Process all nodes
        while n:
            n.print()
            n = n.next

    def find(self, data):
        #Get first node
        n = self.first

        #Process all nodes
        while n:
            #Identical data
            if data == n.data:
                print('Found')
                return n
            n = n.next
        print('Not found')
        return None

    def insert (self, m, data):
        n = Node (data)

        #Link m and n
        n.next = m.next
        m.next = n

    def delete (self, n):
        #Successor
        m = n.next

        #Copy data
        n.data = m.data

        #Create new link
        n.next = m.next

        m = None

#Stack
class Stack:
    def __init__(self):
        self.first : Node = None
        self.last: Node = None

    def push (self, data):
        #Create new node
        n = Node(data)

        #list is empty
        if self.first == None:
            self.first = n
            self.last = n

        #Connect to the last node
        else:
            self.last.next = n
            n.prev = self.last
            self.last = n

    def pop (self):
        #Stack is empty
        if self.first == None:
            return

        #Stack contains 1 elemnt
        elif (self.first == self.last):
            self.first = None
            self.last = None

        #Stack contains multiple elements
        else:
            n = self.last
            self.last = n.prev
            self.last.next = None
            n = None

    def print(self):
        print('Stack:')
        #Get first node
        n = self.first

        #Process all nodes
        while n:
            n.print()
            n = n.next

#Stack
class Queue:
    def __init__(self):
        self.first : Node = None
        self.last: Node = None

    def push (self, data):
        #Create new node
        n = Node(data)

        #list is empty
        if self.first == None:
            self.first = n
            self.last = n

        #Connect behind the last node
        else:
            self.last.next = n
            n.prev = self.last
            self.last = n

    def pop (self):

        #Stack is empty
        if self.first == None:
            return

        #Stack contains 1 elemnt
        elif (self.first == self.last):
            self.first = None
            self.last = None

        #Stack contains multiple elements
        else:
            n = self.first
            self.first = n.next
            self.first.prev = None
            n = None

    def print(self):
        print('Queue:')
        #Get first node
        n = self.first

        #Process all nodes
        while n:
            n.print()
            n = n.next



#Create single-linked list
L = LList()
L.push('1')
L.push('2')
L.push('3')
L.push('4')

#Print and find
L.print()
n = L.find('3')
n.print()

#Insert node
m = L.find('3')
L.insert(m, '5')
L.print()

#Delete node
L.delete(m)
L.print()

#Create stack
S = Stack()
S.push('1')
S.push('2')
S.push('3')
S.push('4')
S.print()
S.pop()
S.print()
S.pop()
S.print()

#Create queue
Q = Queue()
Q.push('1')
Q.push('2')
Q.push('3')
Q.push('4')
Q.print()
Q.pop()
Q.print()
Q.pop()
Q.print()

