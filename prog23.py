class Heap:
    def __init__(self, max_size):
        self.n = 0
        self.h = [0] * (max_size + 1)

    def fhu(self, i):
        #Fix heap up
        while (i > 1) and (self.h[i] < self.h[i//2]):
            #Swap h[i] and h[i//2]
            temp =  self.h[i//2]
            self.h[i // 2] =  self.h[i]
            self.h[i] = temp

            #Go to parent
            i = i//2

    def fhd(self, i):
        # Fix heap up
        while (2 * i < self.n):
            #Swap index points to left parent
            k = 2 * i

            #Test, whether h[k+1] < h[k]
            if k < self.n and self.h[k+1] < self.h[k]:
                k = k + 1

            #Test h[i] and h[k], swap
            if self.h[i] > self.h[k]:
                # Swap h[i] and h[k]
                temp = self.h[k]
                self.h[k] = self.h[i]
                self.h[i] = temp

            #Condition satisfied
            else:
                break

            #Go to parent
            i = k

    def push(self, item):
        #Increment n
        self.n = self.n + 1

        #Connect to heap
        self.h[self.n] = item

        #Fix heap up
        self.fhu(self.n)

    def min(self):
        return self.h[1]

    def max(self):
        x_max = self.h[self.n//2]

        for i in range(self.n//2 + 1 , self.n+1):
            if x_max < self.h[i]:
                x_max = self.h[i]

        return x_max

    def delRoot(self):
        #Swat h[1] and h[n]
        temp = self.h[self.n]
        self.h[self.n] = self.h[1]
        self.h[1] = temp

        #Decrease length of the heap
        self.n = self.n - 1

        #Fix heap down from new root
        self.fhd(1)


#Create heap
h = Heap(50)

#Add element
h.push(3)
h.push(1)
h.push(5)
h.push(6)
h.push(0)

#Find minimum
min = h.min()
print(min)

#Find maximum
max = h.max()
print(max)

#Delete root
h.delRoot()

#Find minimum
min = h.min()
print(min)

#Delete root
h.delRoot()

#Find minimum
min = h.min()
print(min)

#Delete root
h.delRoot()

#Find minimum
min = h.min()
print(min)

#Delete root
h.delRoot()

#Find minimum
min = h.min()
print(min)

