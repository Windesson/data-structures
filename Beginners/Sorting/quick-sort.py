# all items to the left are sorted

def quickSortAscending(arr):
    if len(arr) < 2:
        return arr
    
    for i in range(1,len(arr)):
        j = i - 1 
        while j >= 0 and arr[j + 1] < arr[j]:
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp 

            j -= 1
        
    return arr

def caseTest1(arr):
    temp = arr[:]
    temp.sort()
    actual = quickSortAscending(arr)
    if temp == actual:
        print("pass")
    else:
        print("failed")

caseTest1([3,2,1])

