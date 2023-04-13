def quickSort(X, l , r):
    #Find pivot: mid element
    m = (l + r) // 2
    p = X[m]

    #Initialize indices
    i = l
    j = r

    #Find all elements incorrect according to pivot
    while i <= j:
        #Find first element X[i] larger than pivot
        while X[i] < p:
            i = i + 1

        # Find first element X[j] smaller than pivot
        while X[j] > p:
            j = j - 1

        #Swap X[i] <-> X[j]
        if i <= j:
            temp = X[i]
            X[i] = X[j]
            X[j] = temp

            #Increment/decrement index
            i = i + 1
            j = j - 1

    #Partition, left subset
    if l < j:
        quickSort(X, l, j)

    # Partition, right subset
    if i < r:
        quickSort(X, i, r)

def mergeSort(X, l, r) :
    #Merge sort
    m = (l + r) // 2

    #Stop, if a subset has one element
    if  l == r:
        return

    #Process both parts separately
    mergeSort(X, l, m)
    mergeSort(X, m+1, r)

    #Merge both parts
    merge(X, l, m, r)


def merge(X, l, m, r):
    #Merge two sorted subsets into one sorted
    i = 0
    j = 0

    #Create supplementary arrays
    a = X[l:m+1]
    b = X[m+1:r+1]
    n = len(a)
    m = len(b)

    #Merge procedure
    for k in range (l, r + 1):
        #We rached end of the first subset
        if i == n:
            X[k] = b[j];
            j = j + 1
            continue

        # We rached end of the second subset
        if j == m:
            X[k] = a[i];
            i = i + 1
            continue

        #If a[i] < b[j], take the smaller element
        if a[i] < b[j]:
            X[k] = a[i]
            i = i + 1

        # If b[j] < a[i], take the smaller element
        else:
            X[k] = b[j]
            j = j + 1


X = [1, 6, -5, 13, 8]
#quickSort(X, 0, len(X)-1)
mergeSort(X, 0, len(X)-1)
print(X)