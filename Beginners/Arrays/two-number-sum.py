def twoNumberSum(array, targetSum):
    # Write your code here.
    array = sorted(array)
    l = 0
    r = len(array) - 1
    while array[l] < array[r]:
        temp = array[l] + array[r]
        if temp == targetSum:
            return [array[l], array[r]]
        elif temp < targetSum:
            l += 1
        else:
            r -= 1
    return []