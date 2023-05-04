class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def preoder(self, u):
        if u == None:
            return
        else:
            print(u.data)
            self.preoder(u.left)
            self.preoder(u.right)

    def insert(self, u, data):
        if u == None:
            u = TNode(data)
        else:
            if data < u.data:
                u.left = self.insert(u.left, data)
            elif data > u.data:
                u.right = self.insert(u.right, data)
            else:
                return None
        return u

    def insertNode(self, data):
        self.root = self.insert(self.root, data)
        return self.root

    def Print(self):
        self.preoder(self.root)

    def find(self, data, u):
        if u == None:
            return None
        if data == u.data:
            return u
        if data < u.data:
            return self.find(data, u.left)
        else:
            return self.find(data, u.right)

    def find2(self, data, p : TNode, u : TNode ):
        if u == None:
            return None
        if data == u.data:
            return u
        p[0] = u
        if data < u.data:
            return self.find(data, u.left)
        else:
            return self.find(data, u.right)

    def findNode(self, data):
        return self.find(data, self.root)

    def findNode2(self, p : TNode, data):
        return self.find2(data, p, self.root)

    def clear(self, u : TNode ):
        if u != None:
            self.clear(u.left)
            self.clear(u.right)
            u = None

    def deleteNode (self, data):
        #Find node and its predecessor
        p : TNode  = [None]
        u = bst.findNode2(p, data)

        #Node has not been found
        if u == None:
            return

        #Node is leaf
        if u.left == None and u.right == None:
            self.deleteLeaf(p, u)

        #Node has 1 subtree
        elif u.left == None or u.right == None:
            self.delete1Subtree(p, u)

        #Node has 2 subtrees
        else:
            self.delete2Subtrees(u)

    def deleteLeaf(self, p : TNode,  u : TNode):
        #Delete single leaf

        #Node u is root
        if p == None:
            self.root = None

        #Node is not root
        else:
            if u == p.left:
                p.left = None
            else:
                p.right = None

    def delete1Subtree(self, p : TNode , u: TNode ):
        #Delete 1 subtree of u
        w : TNode = None

        #Node w is the left child of u
        if u.left != None:
            w = u.left

        #Node w is the right child of u
        else:
            w = u.right

        #Node is the root
        if p == None:
            self.root = w

        #Node u is is the left child of p
        if u == p.left:
            p.left = w
        else:
            p.right = w

    def delete2Subtrees(self, u: TNode):
        #Delete 2 subtrees of u, variant PL
        w = u.left
        p = w

        #Find right-most node and its predecessor
        while w.right != None:
            p = w
            w = w.right

        #Swap u<=>v
        u.data = w.data

        #Delete w, leaf
        if w.left == None and w.right == None:
            self.deleteLeaf(p, w)

        #Delete one subtree
        else:
            self.delete1Subtree(p, w)


bst = BST()
bst.insertNode(15)
bst.insertNode(13)
bst.insertNode(25)
bst.Print()

p = [None]
u = bst.findNode2(p, 25)
if u != None:
    print(u.data)
    print(p[0].data)
else:
    print('Not found')

bst.deleteNode (25)
bst.Print()

