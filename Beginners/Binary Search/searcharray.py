
def search(nums, target) -> int:
    L, R = 0, len(nums) - 1

    while L <= R:
        mid = (L + R)// 2

        if target > nums[mid]:
            L = mid + 1 
        elif target < nums[mid]:
            R = mid - 1
        else: 
            return mid

    return -1

#test [-1,0,3,5,9,12] return 4
expected = 4
actual = search([-1,0,3,5,9,12], 9)
if expected == actual:
    print(f"Output: {actual} - pass")
else:
    print(f"Output: {actual} - failed") 