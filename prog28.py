def insertionSort(x):
    for i in range(len(x)):
        #Inserted element
        p = x[i]
        j = i

        #Insert element into the correct place
        while j > 0 and x[j-1] > p:
            #Swap variables
            t = x[j]
            x[j] = x[j-1]
            x[j-1] = t

            #Decrement j
            j = j - 1

def insertionSort2(x):
    for i in range(len(x)):
        #Inserted element
        p = x[i]
        j = i

        #Insert element into the correct place
        while j > 0 and x[j-1] > p:
            #Swap variables
            x[j] = x[j-1]

            #Decrement j
            j = j - 1

        #Write p to the correct position
        x[j] = p

def bubbleSort(x):
    for i in range (len(x)):
        #for j in range(len(x)):
        for j in range(len(x) - 1,  i, -1):
            #Incorrect order
            if x[j-1] > x[j]:
                # Swap variables
                t = x[j]
                x[j] = x[j - 1]
                x[j - 1] = t

def bubbleSort2(x):
    for i in range (len(x)):
        for j in range(len(x)-1 - i):
            #Incorrect order
            if x[j] > x[j+1]:
                # Swap variables
                t = x[j]
                x[j] = x[j + 1]
                x[j + 1] = t

def bubbleSort3(x):
    #Assumption
    sorted = False
    i = 0

    #Repeat until x is sorted
    while not (sorted):

        #Assumption, x is sorted
        sorted = True
        for j in range(len(x) - 1,  i, -1):
            #Incorrect order
            if x[j-1] > x[j]:
                # Swap variables
                t = x[j]
                x[j] = x[j - 1]
                x[j - 1] = t

                #Swap, x is not sorted
                sorted = False

        i = i + 1


x = [1, -7, 35, 4, 19, 0, -6]
#insertionSort2(x)
bubbleSort3(x)
print(x)
