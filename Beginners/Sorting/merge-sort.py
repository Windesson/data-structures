

# left and right side are already sorted. 
# this merges two sorted sides of the array
def merge(arr, s, m, e):
    
    i = s
    j = m + 1
    
    temp = []
    
    while i <= m and j <= e:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1;
        else:
            temp.append(arr[j])
            j += 1;
            
    while j <= e:
        temp.append(arr[j])
        j += 1;
            
    while i <= m:
        temp.append(arr[i])
        i += 1;

    for item in temp:
        arr[s] = item;
        s += 1
           
# Divide and conquer approach
def mergeSort(arr, s, e):
    
    if e - s + 1 <= 1:
        return arr;
    
    m = (s+e)//2
    mergeSort(arr, s, m)
    mergeSort(arr, m +1 , e)
    
    merge(arr, s, m, e)
    
    return arr
    

print(mergeSort([1,2,5,4,3], 0, 4))

    