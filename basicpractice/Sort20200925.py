def insertsort(arr):
    for i in range(1, len(arr)):
        v = arr[i]
        j = i-1
        while j >= 0:
            if arr[j] > v:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break

        arr[j+1] = v
    print arr

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

def selectionsort(arr):
    for i in range(len(arr)):
        min = arr[i]
        minidx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    print(arr)

def mergesort(arr):

    def merge(s1, e1, s2, e2):
        res = []
        i1, i2 = s1, s2
        while i1 <= e1 and i2 <= e2:
            if arr[i1] < arr[i2]:
                res.append(arr[i1])
                i1 += 1
            else:
                res.append(arr[i2])
                i2 += 1
        res.extend(arr[i1:e1+1] if i1 <=e1 else arr[i2:e2+1])
        arr[s1:e2+1] = res[:]

    def helper(s, e):
        if s == e:
            return
        mid = (s + e)//2
        helper(s, mid)
        helper(mid +1, e)
        merge(s, mid, mid + 1, e)

    helper(0, len(arr) - 1)
    print(arr)

def quicksort(arr):

    def helper(s, e):
        if s >= e: return
        pivot = partation(s, e)
        helper(s, pivot - 1)
        helper(pivot + 1, e)


    def partation(s, e):
        pivot = arr[e]
        i, j = s, s
        while i < e:
            if arr[i] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1
            i += 1
        arr[j], arr[e] = arr[e], arr[j]
        return j

    helper(0, len(arr) - 1)
    print(arr)

arr = [5,3,4,1,2]
#quicksort([2,3,4,1,5])
#bubblesort(arr)
#selectionsort(arr)
#mergesort(arr)
quicksort(arr)
