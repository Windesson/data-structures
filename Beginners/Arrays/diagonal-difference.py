def diagonalDifference(arr):
    # Write your code here
    left_to_right = 0
    right_to_left = 0
    for i in range(len(arr)):
        left_to_right += arr[i][i]
        right_to_left += arr[i][len(arr)-1-i]
    
    res = left_to_right - right_to_left
    return abs(res)